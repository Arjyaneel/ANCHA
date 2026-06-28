def score_memory(
    memory,
    current_message
):
    """
    Compute a simple relevance score.
    """

    relevance = 0

    message = current_message.lower()

    content = memory["memory_content"].lower()

    for word in message.split():

        if word in content:

            relevance += 1

    importance = memory["importance_score"]

    final_score = relevance + importance

    return {

        "memory": memory,

        "relevance_score": relevance,

        "importance_score": importance,

        "final_score": final_score

    }


def rank_memories(
    memories,
    current_message
):
    """
    Rank memories by final score.
    """

    ranked = [

        score_memory(
            memory,
            current_message
        )

        for memory in memories

    ]

    ranked.sort(

        key=lambda item:
        item["final_score"],

        reverse=True
    )

    return ranked