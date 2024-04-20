from flask import Flask, request
from pytube import YouTube

# example video id: Up5Gm_Ls2oQ

def get_data(url: str):
  try:
    ytd = YouTube(url)
    print(url)
    return {
      "title": ytd.title,
      "author": ytd.author,
      "thumbnail_url": ytd.thumbnail_url,
      "channel_url": ytd.channel_url,
      "length_seconds": ytd.length,
      "keywords": ytd.keywords,
      "publish_data": ytd.publish_date,
      "views": ytd.views
    }
  except:
    return {
      "message": "Invalid URL"
    }

app = Flask(__name__)

@app.route("/")
def index():
  url = request.args.get("url")
  if url:
    return get_data(url)
  else:
    return {
      "message": "Please provide a valid URL in the URL params"
    }

@app.route("/<id>")
def vid_id_route(id):
  return get_data(id)