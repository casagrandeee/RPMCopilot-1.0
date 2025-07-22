import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.runnables import Runnable
from backend.services.history import get_session_history
from backend.services.prompts import *

llm = ChatOpenAI(
    api_key= os.getenv("OPENAI_API_KEY"),
    streaming=True,
    temperature=0.7,
    model="gpt-4o-mini",
)

prompt = ChatPromptTemplate.from_messages([
    ("system", AGENT_PROMPT),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

chain: Runnable = prompt | llm

chat_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_message_key="question",
    history_message_key="history"
)