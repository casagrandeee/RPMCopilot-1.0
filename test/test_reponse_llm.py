import requests

username: str = input("Enter your username: ")

while True:
    question: str = input("(you) : ")

    response = requests.post(
        "http://localhost:8000/api/v1/agent/stream-chat",
        json={
            "name": username,
            "question": question
        },
        stream=True
    )

    print ("(agent) : ", end="", flush=True)
    for chunk in response.iter_content(chunk_size=None):
        print (chunk.decode(), end="", flush=True)

    print()