from app.database.memory_model import get_memories

user_id = int(input("Enter User ID: "))

memories = get_memories(user_id)

for memory in memories:
    print(dict(memory))