import os
import config

from fastapi import APIRouter, Form
from twilio.rest import Client

# Get setting variables
settings = config.Settings()

# router
router = APIRouter()

@router.post("/send_sms")
def send_sms(to_number: str = Form(...), body: str = Form(...)):
    print(to_number)
    client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
    message = client.messages.create(from_=settings.twilio_phone_number, to=to_number, body=body)
    return {"message_sid": message.sid, "status": message.status}
    