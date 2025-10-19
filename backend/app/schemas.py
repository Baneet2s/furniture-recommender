from pydantic import BaseModel, Field
from typing import List, Optional, Dict


class Message(BaseModel):
role: str
content: str


class ChatRequest(BaseModel):
session_id: str
messages: List[Message]


class Product(BaseModel):
uniq_id: str
title: str
brand: Optional[str] = None
description: Optional[str] = None
price: Optional[float] = None
categories: Optional[List[str]] = None
images: Optional[List[str]] = None
metadata: Optional[Dict] = None


class RecommendResponse(BaseModel):
results: List[Product]


class AnalyticsSummary(BaseModel):
n_items: int
brands_top: List[Dict]
categories_top: List[Dict]
price_stats: Dict
