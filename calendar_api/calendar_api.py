import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'calendar_api/credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)
CALENDAR_ID = os.getenv("CALENDAR_ID")

def get_availability(day):
    return f"You are free between 2PM - 5PM on {day.capitalize()}"

def book_slot(date_str, time_range):
    event = {
        'summary': 'Meeting booked by TailorTalk',
        'start': {'dateTime': '2025-06-26T15:00:00', 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': '2025-06-26T16:00:00', 'timeZone': 'Asia/Kolkata'},
    }
    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return f"Booked: {event.get('htmlLink')}"
