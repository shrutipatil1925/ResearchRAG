from backend.rag.session_manager import (
    create_chat_session,
    load_session_history,
    save_session_history
)


session_name = "test_chat"

create_chat_session(session_name)


history = load_session_history(session_name)

print("\nBefore:")
print(history)


history.append(
    (
        "What is RAG?",
        "RAG stands for Retrieval-Augmented Generation."
    )
)


save_session_history(
    session_name,
    history
)


history = load_session_history(session_name)

print("\nAfter:")
print(history)