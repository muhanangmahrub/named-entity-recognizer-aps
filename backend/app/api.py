from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from inference.predict import predict_text

app = FastAPI()

class TextRequest(BaseModel):
    text: str
    model: str

origins = [
    'http://localhost:5173',
    'localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {'message': "Welcome to your Named Entity App."}

@app.post("/predict", tags=['predict'])
async def inference_text(request: TextRequest):
    entities = predict_text(request.model, request.text)
    return entities