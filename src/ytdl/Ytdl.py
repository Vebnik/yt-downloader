# libs
import youtube_dl

# moduel
from src.models.ytdl import Video

class Ytdl(youtube_dl.YoutubeDL):

  def __init__(self, hooks, auto_init=True):
    params = { 'progress_hooks': [hooks] }
    super().__init__(params, auto_init)
  
  def __enter__(self):
    return super().__enter__()

  def __exit__(self, *args):
    return super().__exit__(*args)

  def get_info(self, url: str) -> Video:
    try:
      return Video(self.extract_info(url, download=False))
    except Exception as ex:
      print(ex)

