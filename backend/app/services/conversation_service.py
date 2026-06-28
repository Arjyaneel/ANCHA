from Backend.app.services.reflection_scheduler import should_reflect
from app.database.chat_model import (
    save_message
)

from app.services.reflection_service import (
    process_reflections
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

from app.services.journal_service import (
    process_journal
)

from app.services.followup_service import (
    process_followups
)

from app.ai.gemini_service import (
    analyze_emotion
)

from app.services.ai_context_service import build_user_context

from app.services.memory_service import (
    process_memory
)
from app.services.pattern_service import (
    process_patterns
)

from app.services.recommendation_service import (
    build_recommendations
)
from app.services.reflection_scheduler import (
    should_reflect
)

def process_message(
    user_id,
    text
):

    save_message(
        user_id,
        "user",
        text
    )

    
    context = build_user_context(
        user_id
    )
    

    ai_response = analyze_emotion(
        text,
        context
    )
 
    save_message(
        user_id,
        "assistant",
        ai_response["support_response"]
    )
    process_memory(
        user_id,
        text
    )

    
    process_journal(
        user_id,
        text,
        ai_response
    )

    process_patterns(
    user_id
    )

    
    if should_reflect(user_id):

        process_reflections(
        user_id
        )

    process_followups(
        user_id,
        text
    )

    return ai_response
   
    

   
