import os
import requests
import feedparser
from telegram import Bot

# Get secrets from environment variables
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

FEED_URL = "https://www.cisa.gov/sites/default/files/cyber-alerts.xml"

def fetch_news():
    feed = feedparser.parse(FEED_URL)
    if not feed.entries:
        return
    
    latest_entry = feed.entries[0]
    title = latest_entry.title
    link = latest_entry.link

    message = f"🚨 *Latest Cyber Alert* 🚨\n\n*{title}*\n[Read More]({link})"
    
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

if __name__ == "__main__":
    fetch_news()
