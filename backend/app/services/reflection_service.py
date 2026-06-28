from app.ai.reflection_generator import (
    generate_reflections
)

from app.database.journal_model import (
    get_recent_entries
)

from app.database.memory_model import (
    get_memories
)

from app.database.pattern_model import (
    get_patterns
)

from app.database.reflection_model import (
    reflection_exists,
    save_reflection,
    update_reflection
)


def process_reflections(user_id):
    """
    Generate long-term reflections
    and store them.
    """

    journals = get_recent_entries(
        user_id,
        10
    )

    memories = get_memories(
        user_id
    )

    patterns = get_patterns(
        user_id
    )

    result = generate_reflections(
        journals,
        memories,
        patterns
    )

    reflections = result.get(
        "reflections",
        []
    )

    for item in reflections:

        title = item["title"]

        if reflection_exists(
            user_id,
            title
        ):

            update_reflection(
                user_id,
                title,
                item["reflection"],
                item["confidence"]
            )

        else:

            save_reflection(
                user_id,
                title,
                item["reflection"],
                item["confidence"]
            )