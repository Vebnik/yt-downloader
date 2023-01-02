

class Video:

  __slots__ = ('title', 'duration', 'channel', 'formats', 'thumbnail')

  def __init__(self, data: dict) -> None:
    self.title: int = data.get('title')
    self.duration: int = data.get('duration')
    self.channel: int = data.get('channel')
    self.formats: list[dict] = [{item.get('format'): item.get('url')} for item in data.get('formats')]
    self.thumbnail: str = data.get('thumbnail')



