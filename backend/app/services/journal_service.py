from app.database.journal_model import (
    save_entry
)


def process_journal(
    user_id,
    text,
    ai_response
):
    """
    Save the current conversation as a journal entry.
    """

    save_entry(
        user_id,
        text,
        ai_response["emotion"],
        ai_response["energy_level"],
        ai_response["mood_summary"],
        ai_response["support_response"],
        str(ai_response["tips"])
    )