import json
import os
from googleapiclient.discovery import build

import isodate


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def get_response(self):
        request = self.youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=self.channel_id
        )
        response = request.execute()

        return response

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(Channel.get_response(self), indent=2, ensure_ascii=False))
