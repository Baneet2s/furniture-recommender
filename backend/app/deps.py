import os
from fastapi.middleware.cors import CORSMiddleware


def add_cors(app):
origin = os.getenv('FRONTEND_ORIGIN', 'http://localhost:5173')
app.add_middleware(
CORSMiddleware,
allow_origins=[origin],
allow_methods=['*'],
allow_headers=['*'],
allow_credentials=True,
)
