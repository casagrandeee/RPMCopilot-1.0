from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from backend.services.chat_stream import stream_chat

router = APIRouter(prefix="/agent")

@router.post("/stream-chat")
async def stream_chat(request: Request):
    body:dict = await request.json()
    username = body.get("name")
    question = body.get("question")

    return StreamingResponse(
        stream_chat(username, question),
        media_type="text/plain"
    )