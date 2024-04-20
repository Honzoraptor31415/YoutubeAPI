from flask import Flask, request, redirect
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
      "message": "Please provide a valid URL in the URL params."
    }
  
@app.route("/github")
def github():
  return redirect("https://github.com/Honzoraptor31415/YoutubeAPI", code=302)

@app.route("/author")
def author():
  return redirect("https://github.com/Honzoraptor31415", code=302)