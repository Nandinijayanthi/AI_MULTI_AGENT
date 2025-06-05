import re

def extract_email_metadata(email_body: str) -> dict:
    sender = re.findall(r"From:\\s*(.*)", email_body)
    urgency = "High" if "urgent" in email_body.lower() else "Normal"
    intent = "RFQ" if "quote" in email_body.lower() else "Other"
    conversation_id = str(hash(email_body[:50]))

    return {
        "sender": sender[0] if sender else "Unknown",
        "intent": intent,
        "urgency": urgency,
        "conversation_id": conversation_id
    }
