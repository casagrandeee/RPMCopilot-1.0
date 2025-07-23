from fastapi import APIRouter
from fastapi.responses import JSONResponse
from backend.services.history import ChatHistory

router = APIRouter(prefix="/chat")

@router.get("/get-history")
async def get_history(username: str):
    chat = ChatHistory(username)
    return JSONResponse(
        content=chat.get_history(),
        status_code=200
    )

@router.get("/get-chats")
async def get_chats():
    chat = ChatHistory("")
    return JSONResponse(
        content=chat.get_chats(),
        status_code=200
    )