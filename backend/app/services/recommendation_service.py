from app.database.memory_model import (
    get_top_memories
)

from app.database.followup_model import (
    get_pending_followups
)

from app.database.pattern_model import (
    get_patterns
)

from app.database.journal_model import (
    get_recent_entries
)


def build_recommendations(
    user_id
):

    memories = get_top_memories(
        user_id,
        5
    )

    patterns = get_patterns(
        user_id
    )

    followups = get_pending_followups(
        user_id
    )

    journals = get_recent_entries(
        user_id,
        5
    )

    return {

        "memories": memories,

        "patterns": patterns,

        "followups": followups,

        "journals": journals

    }