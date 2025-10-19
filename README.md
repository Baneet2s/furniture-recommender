# Product Recommendation Web App (FastAPI + React + Pinecone + LangChain)

A full-stack, ML-driven furniture recommendation application that combines ML, NLP, CV, and GenAI with a vector database.

## Features
- Conversational recommendation page powered by embeddings + retrieval + lightweight LLM.
- Text clustering to group similar products.
- Image classification using CLIP zero-shot or fine-tuned CNN.
- Generative descriptions for recommended items.
- Vector DB (Pinecone) storing text & image embeddings for semantic search.
- Analytics page with dataset insights.
- LangChain for LLM and embedding pipelines.

## Tech
- Backend: FastAPI, Uvicorn
- Vector DB: Pinecone
- Embeddings: sentence-transformers, OpenAI/LLM-compatible or Instructor models; image via CLIP
- GenAI: Any small open-source LLM through LangChain (e.g., llama.cpp/ollama/local), or API
- CV: OpenAI CLIP zero-shot or torchvision ResNet fine-tune
- Frontend: React + Vite + Tailwind (optional)
- Analytics/Training: Jupyter notebooks

## Quickstart

### 1) Backend
```
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # fill keys
uvicorn app.main:app --reload
```

### 2) Frontend
```
cd frontend
npm install
npm run dev
```

### 3) Notebooks
Open `notebooks/analytics.ipynb` and `notebooks/train_models.ipynb` in Jupyter/VS Code.

## Environment
Create `backend/.env` from the example and add at least:
```
PINECONE_API_KEY=your_key
PINECONE_ENV=your_env
PINECONE_INDEX=products-index
EMBEDDING_MODEL=text-embedding-3-small  # or 'all-MiniLM-L6-v2'
IMAGE_EMBED_MODEL=ViT-L/14
LLM_MODEL=ollama:llama3.1:8b  # or 'gpt-4o-mini' etc
```

## API (selected)
- `POST /ingest` — embed products (text + images) and upsert into Pinecone.
- `POST /recommend/chat` — conversational recommender, returns product list + generated descriptions.
- `GET /analytics/overview` — lightweight stats for the analytics page.
- `POST /classify/image` — classify an image to a category using CLIP or a fine-tuned CNN.

## Notes
- Start with CLIP zero-shot for image categories; optionally fine-tune ResNet if time permits.
- Keep prompts lightweight and safe; cache embeddings locally when developing.
- Ensure `uniq_id` is used as the primary key across systems.
