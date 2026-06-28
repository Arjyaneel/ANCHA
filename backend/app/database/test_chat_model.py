from app.database.chat_model import (
    save_message,
    get_recent_chat
)

save_message(
    4,
    "user",
    "Hello Ancha"
)

save_message(
    4,
    "assistant",
    "Hello! How are you feeling today?"
)

messages = get_recent_chat(4)

print("\nCHAT HISTORY:\n")

for message in messages:

    print(
        message["role"],
        ":",
        message["message"]
    )