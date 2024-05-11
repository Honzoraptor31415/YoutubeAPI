from flask import Flask, request, redirect
from pytube import YouTube, Channel, Playlist

invalid_url_msg = "Please provide a valid URL"

def get_data(url: str):
  try:
    dot_split = url.split(".")
    dot_split_last = dot_split[len(dot_split)-1]
    url_route = dot_split_last.split("/")[1].split("?")[0]
    
    if url_route == "channel":
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
      "message": "Something went wrong"
    }
    
  
def get_vid_data(url: str):
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

def get_channel_data(url: str):
  ytc = Channel(url)
  print(f"\nChannel data:\n\n{ytc}")
  return {
    "type": "channel",
    "channel_name": ytc.channel_name
  }

def get_playlist_data(url: str):
  try:
    ytp = Playlist(url)
    return {
      "type": "playlist",
      "video_urls": ytp
    }
  except:
    return {
      "message": "Something went wrong"
    }


app = Flask(__name__)

@app.route("/")
def index():
  print(request.url)
  url = request.args.get("url")
  if url:
    return get_data(url)
  else:
    return {
      "message": f"{invalid_url_msg}, or take a look at /author for more info about the creator or /github for source code.",
      "valid_url_example": "/?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }
  
@app.route("/github")
def github():
  return redirect("https://github.com/Honzoraptor31415/YoutubeAPI", code=302)

@app.route("/author")
def author():
  return redirect("https://github.com/Honzoraptor31415", code=302)