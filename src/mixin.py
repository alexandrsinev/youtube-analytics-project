import os
from googleapiclient.discovery import build


class APIMixin:
    api_key: str = os.getenv('YT_API_KEY')

    @classmethod
    def get_service(cls):
        service = build('youtube', 'v3', developerKey=cls.api_key)
        return service
