from app.database.chat_model import (
    get_checkin_count
)


def should_reflect(
    user_id
):
    """
    Decide whether reflections
    should be regenerated.
    """

    count = get_checkin_count(
        user_id
    )

    return count % 10 == 0