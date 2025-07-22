from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.v1.agent import router as agent_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(agent_router, prefix="/api/v1")