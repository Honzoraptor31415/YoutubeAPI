from flask import Flask, request, redirect
from pytube import YouTube
import re

# example video id: Up5Gm_Ls2oQ

invalid_url_msg = "Please provide a valid URL"

def get_data(url: str):
  try:
    dot_split = url.split(".")
    dot_split_last = dot_split[len(dot_split)-1]
    url_route_1stchar = dot_split_last.split("/")[1][0]
    url_route = dot_split_last.split("/")[1].split("?")[0]
    
    if url_route_1stchar == "@":
      return get_channel_data(url)
    elif url_route == "watch":
      return get_vid_data(url)
    elif url_route == "playlist":
      return get_playlist_data(url)
    else:
      return {
        "message": invalid_url_msg
      }
    
  except:
    return {
      "message": invalid_url_msg
    }
    
  
def get_vid_data(url: str):
  try:
    ytd = YouTube(url)
    print(url)
    return {
      "type": "video",
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
      "message": invalid_url_msg
    }

def get_channel_data(url: str):
  # ytd = YouTube(url)
  # print(url)
  return {
    "type": "channel"
    # "title": ytd.title,
    # "author": ytd.author,
    # "thumbnail_url": ytd.thumbnail_url,
    # "channel_url": ytd.channel_url,
    # "length_seconds": ytd.length,
    # "keywords": ytd.keywords,
    # "publish_data": ytd.publish_date,
    # "views": ytd.views
  }

def get_playlist_data(url: str):
  return {
    "type": "playlist"
  }

app = Flask(__name__)

@app.route("/")
def index():
  url = request.args.get("url")
  if url:
    return get_data(url)
  else:
    return {
      "message": invalid_url_msg
    }
  
@app.route("/github")
def github():
  return redirect("https://github.com/Honzoraptor31415/YoutubeAPI", code=302)

@app.route("/author")
def author():
  return redirect("https://github.com/Honzoraptor31415", code=302)