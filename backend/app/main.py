import os
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import List
from .schemas import ChatRequest, RecommendResponse, Product, AnalyticsSummary
from .recommender import Recommender
from .nlp_utils import TextClusterer
from .cv_model import ImageClassifier
from .utils import load_dataset_csv


app = FastAPI(title='Furniture Recommender')


# CORS
from .deps import add_cors
add_cors(app)


# Globals
EMBED_MODEL = os.getenv('EMBEDDING_MODEL', 'sentence-transformers/all-MiniLM-L6-v2')
DATA_PATH = os.getenv('DATA_PATH', 'backend/data/furniture.csv')
LABEL_MAP = 'backend/models/label_map.json'
IMG_WEIGHTS = 'backend/models/image_classifier.pt'


reco = Recommender(EMBED_MODEL)
clusterer = TextClusterer(k=12)


# Lazy load dataset and fit NLP clusters
rows = load_dataset_csv(DATA_PATH)
reco.ingest(rows)
cluster_docs = [" ".join([r.get('title',''), r.get('description','')]) for r in rows]
try:
clusterer.fit(cluster_docs)
except Exception:
pass


try:
cvclf = ImageClassifier(IMG_WEIGHTS, LABEL_MAP)
except Exception:
cvclf = None


@app.get('/')
def root():
return {'ok': True, 'message': 'Furniture Recommender API'}


@app.post('/chat/recommend', response_model=RecommendResponse)
def chat_recommend(req: ChatRequest):
last = req.messages[-1].content if req.messages else ''
items = reco.recommend(last, k=6)
products = [Product(**{
'uniq_id': r.get('uniq_id',''),
'title': r.get('title',''),
'brand': r.get('brand'),
'description': r.get('gen_description', r.get('description')),
