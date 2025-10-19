from typing import List, Dict
from .vectorstore import VectorIndex
from .genai import GenDesc


class Recommender:
def __init__(self, embed_model: str):
self.index = VectorIndex(embed_model)
self.gen = GenDesc()
self.rows: List[Dict] = []


def ingest(self, rows: List[Dict]):
self.rows = rows
self.index.build(rows)


def recommend(self, query: str, k:int=6) -> List[Dict]:
recs = self.index.query(query, k=k)
for r in recs:
r.setdefault('material', '')
r.setdefault('color', '')
r['gen_description'] = self.gen.describe(
r.get('title',''), r.get('brand',''), r.get('material',''), r.get('color','')
)
return recs
