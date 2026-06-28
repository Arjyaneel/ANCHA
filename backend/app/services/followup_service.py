from app.database.followup_model import (
    save_followup,
    complete_followup
)


def process_followups(
    user_id,
    text
):

    lower_text = text.lower()

    # Complete Follow-ups

    if (
        "interview went" in lower_text
        or
        "finished interview" in lower_text
    ):

        complete_followup(
            user_id,
            "Interview Tomorrow"
        )


    if (
        "exam went" in lower_text
        or
        "finished exam" in lower_text
    ):

        complete_followup(
            user_id,
            "Exam Tomorrow"
        )


    # Create Follow-ups

    if "interview tomorrow" in lower_text:

        save_followup(
            user_id,
            "Interview Tomorrow",
            "Ask the user how the interview went.",
            "2026-06-22 09:00:00",
            "high"
        )


    if "exam tomorrow" in lower_text:

        save_followup(
            user_id,
            "Exam Tomorrow",
            "Ask the user how the exam went.",
            "2026-06-22 18:00:00",
            "high"
        )


    if "presentation tomorrow" in lower_text:

        save_followup(
            user_id,
            "Presentation Tomorrow",
            "Ask the user how the presentation went.",
            "2026-06-22 18:00:00",
            "normal"
        )


    if "assignment deadline tomorrow" in lower_text:

        save_followup(
            user_id,
            "Assignment Deadline",
            "Ask whether the assignment was submitted.",
            "2026-06-22 18:00:00",
            "high"
        )