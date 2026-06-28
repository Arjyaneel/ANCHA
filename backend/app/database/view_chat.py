from app.database.chat_model import get_recent_chat

messages = get_recent_chat(
    4,
    20
)

print("\nCHAT HISTORY:\n")

for message in messages:

    print(
        message["role"],
        ":",
        message["message"]
    )