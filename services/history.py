import os, json
from typing import List, Union
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

CHATS_DIR = "backend/chats"

def _get_path(session_id: str):
    os.makedirs(CHATS_DIR, f"{session_id}.json")
    return os.path.join(CHATS_DIR, f"{session_id}.json")

class ChatHistory:
    def __init__(self, session_id: str):
        self.path = _get_path(session_id)
        self.messages = self.__load__messages()

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

    def add_messages(self, message: List[Union[BaseMessage, List[BaseMessage]]]):
        flat: List[BaseMessage] = []

        for msg in message:
            if isinstance(msg, list):
                flat.extend(msg)
            else:
                flat.append(msg)

        for m in flat:
            self.messages.append(m)

        return self._save()

    def get_messages(self):
        return self.messages

    def get_history(self):
        if not os.path.isfile(self.path):
            return []

        files = [
            os.path.splitext(filename)[0]
            for filename in os.listdir(CHATS_DIR)
            if filename.endswith(".json")
        ]

        return sorted(files)



    def _save(self):
        data = []
        for m in self.messages:
            role = "user" if isinstance(m, HumanMessage) else "ai"
            data.append({"role": role, "content": m.content})
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)


def get_session_history(session_id:str) -> ChatHistory:
    return ChatHistory(session_id)
