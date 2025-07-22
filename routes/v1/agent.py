from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from backend.services.chat_stream import streaming_chat

router = APIRouter(prefix="/agent")

@router.post("/streaming-chat")
async def straming_chat(request: Request):
    body:dict = await request.json()
    username = body.get("name")
    question = body.get("question")

    return StreamingResponse(
        straming_chat(username, question),
        media_type="text/plain"
    )