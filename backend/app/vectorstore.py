import os
import numpy as np
from typing import List, Dict
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document


class VectorIndex:
def __init__(self, text_model_name: str):
self.embedder = SentenceTransformer(text_model_name)
self.db = None
self.id_map = {} # int -> row


def build(self, rows: List[Dict]):
docs = []
for i, r in enumerate(rows):
text = " \n ".join([
r.get("title", ""),
r.get("brand", ""),
r.get("description", ""),
", ".join(r.get("categories", []) or [])
])
docs.append(Document(page_content=text, metadata={"row": r}))
embeddings = [self.embedder.encode(d.page_content) for d in docs]
self.db = FAISS.from_embeddings([(doc, np.array(e)) for doc, e in zip(docs, embeddings)])


def query(self, text: str, k: int = 6) -> List[Dict]:
e = self.embedder.encode(text)
docs = self.db.similarity_search_by_vector(e, k=k)
return [d.metadata["row"] for d in docs]
