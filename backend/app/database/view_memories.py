from app.database.memory_model import get_memories


memories = get_memories(1)

for memory in memories:
    print(dict(memory))