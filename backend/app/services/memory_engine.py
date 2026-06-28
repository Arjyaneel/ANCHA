from app.database.memory_model import (
    get_memories
)

from app.ai.memory_ranker import (
    rank_memories
)


def retrieve_memories(user_id):
    """
    Retrieve every stored memory
    for a user.
    """

    return get_memories(user_id)


def get_relevant_memories(
    user_id,
    current_message,
    limit=5
):
    """
    Retrieve and rank memories
    for the current conversation.
    """

    memories = retrieve_memories(
        user_id
    )

    ranked = rank_memories(
        memories,
        current_message
    )

    return [

    item["memory"]

    for item in ranked[:limit]

]