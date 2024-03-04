import asyncio
import uvicorn
import sms.send_sms as send_sms
import sms.reply_sms as reply_sms
from fastapi import FastAPI
from pyngrok import ngrok
app = FastAPI()

app.include_router(send_sms.router, tags=["send"])
app.include_router(reply_sms.router, tags=["reply"])

@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8001,reload=True)