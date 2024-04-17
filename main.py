from flask import Flask
from pytube import YouTube

# just an example
author = YouTube("https://www.youtube.com/watch?v=mo1TN-quILs").author

def get_data(id: str):
  return {
    "title": YouTube(f"https://www.youtube.com/watch?v={id}").title,
    "author": YouTube(f"https://www.youtube.com/watch?v={id}").author,
    "thumbnail_url": YouTube(f"https://www.youtube.com/watch?v={id}").thumbnail_url,
    "channel_url": YouTube(f"https://www.youtube.com/watch?v={id}").channel_url,
    "length_seconds": YouTube(f"https://www.youtube.com/watch?v={id}").length
  }

app = Flask(__name__)

@app.route("/<id>")
def index(id):
  return get_data(id)