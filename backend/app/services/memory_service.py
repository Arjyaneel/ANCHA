from app.ai.memory_extractor import (
    extract_memory
)

from app.database.memory_model import (
    save_memory,
    memory_exists
)


def process_memory(
    user_id,
    text
):

    memory = extract_memory(text)

    if not memory["should_save"]:
        return

    already_exists = memory_exists(
        user_id,
        memory["memory_content"]
    )

    if already_exists:
        return

    save_memory(
        user_id,
        memory["memory_type"],
        memory["memory_content"],
        memory["importance_score"]
    )