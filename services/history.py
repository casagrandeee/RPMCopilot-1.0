import os, json
from typing import List, Union
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

CHATS_DIR = "backend/chats"

def __get__path(session_id: str):
    os.makedirs(CHATS_DIR, f"{session_id}.json")
    return os.path.join(CHATS_DIR, f"{session_id}.json")

class ChatHistory:
    def __init__(self, session_id: str):
        self.path = __get__(session_id)
        self.messages = self.

    def __load__messages(self):
        if not os.path.exists(self.path):
            return []

        with open(self.path, "r") as f:
            data = json.load(f)
            return [
                HumanMessage(content=m["content"] if m["role"] == "user"
                else AIMessage(content=m["content"]))
                for m in data
            ]

    def add_message(self, message: List[Union[BaseMessage, List[BaseMessage]]]):
        flat: List[BaseMessage] = []

        for msg in messages:
            if isinstance(msg, list):
                flat.extend(msg)
            else:
                flat.append(msg)

        for m in flat:
            self.messages.append(m)

        return self._save()


    def _save(self):
        data = []
        for m in self.messages:
            role = "user" if isinstance(m, HumanMessage) else "ai"
            data.append({"role": role, "content": m.content}
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)
