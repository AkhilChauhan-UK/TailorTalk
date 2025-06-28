from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.agent import process_input

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message")
    response = await process_input(user_input)
    return {"response": response}
