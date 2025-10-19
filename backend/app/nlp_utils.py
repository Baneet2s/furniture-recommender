from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from typing import List, Dict


class TextClusterer:
def __init__(self, k:int=12):
self.vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
self.kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
self.fitted = False


def fit(self, docs: List[str]):
X = self.vectorizer.fit_transform(docs)
self.kmeans.fit(X)
self.fitted = True


def label(self, docs: List[str]) -> List[int]:
X = self.vectorizer.transform(docs)
return self.kmeans.predict(X).tolist()
