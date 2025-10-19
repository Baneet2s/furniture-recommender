import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import json
from typing import List


class ImageClassifier:
def __init__(self, weights_path: str, label_map_path: str):
self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
self.model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
num_ftrs = self.model.fc.in_features
self.model.fc = nn.Linear(num_ftrs, 10) # will be replaced by trained head
self.model.load_state_dict(torch.load(weights_path, map_location=self.device))
self.model.eval().to(self.device)
with open(label_map_path, 'r') as f:
self.label_map = json.load(f)
self.preprocess = transforms.Compose([
transforms.Resize(256),
transforms.CenterCrop(224),
transforms.ToTensor(),
transforms.Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225])
])


def predict_path(self, img_path: str) -> str:
img = Image.open(img_path).convert('RGB')
x = self.preprocess(img).unsqueeze(0).to(self.device)
with torch.no_grad():
logits = self.model(x)
cls = logits.argmax(dim=1).item()
return self.label_map[str(cls)]
