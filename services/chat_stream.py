from backend.services.llm import chat_chain

async def stream_chat(username: str, question: str):
    response_stream = chat_chain.stream(
        {"question": question},
         config={"configurable": {"session_id": username}}
    )

    for chunk in response_stream:
        content = getattr(chunk, "content", None)
        if content:
            yield content
