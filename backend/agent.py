# backend/agent.py
from calendar_api.calendar_api import get_availability, book_slot

async def process_input(user_input):
    if "tomorrow" in user_input:
        return book_slot("tomorrow", "afternoon")
    elif "free time" in user_input:
        return get_availability("friday")
    elif "between" in user_input:
        return book_slot("next week", "3-5 PM")
    else:
        return "Sorry, I didn't understand. Please rephrase."
