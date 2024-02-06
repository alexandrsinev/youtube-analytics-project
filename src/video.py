import json
from src.channel import Channel


class Video(Channel):

    def __init__(self, video_id):
        """Экземпляр инициализируется id видео."""

        self.video_id = video_id
        self.title = self.get_attributes()['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count = self.get_attributes()['items'][0]['statistics']['viewCount']
        self.number_of_likes = self.get_attributes()['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title}'

    def get_response(self):
        """Получаем статистику видео по его id"""

        video_response = super().get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=self.video_id
                                                             ).execute()

        return video_response

    def get_attributes(self):
        """Получаем из json Python объект из которого будем забирать значения аттрибутов класса"""

        file = json.dumps(self.get_response(), indent=2, ensure_ascii=False)
        new_file = json.loads(file)
        return new_file


class PLVideo(Channel):
    def __init__(self, video_id, playlist_id):
        """Экземпляр инициализируется id видео и id плейлиста."""

        self.video_id = video_id
        self.title = self.get_attributes()['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count = self.get_attributes()['items'][0]['statistics']['viewCount']
        self.number_of_likes = self.get_attributes()['items'][0]['statistics']['likeCount']
        self.playlist_id = playlist_id

    def __str__(self):
        return f'{self.title}'

    def get_response(self):
        """Получаем статистику видео по его id"""

        video_response = super().get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=self.video_id
                                                             ).execute()

        return video_response

    def get_attributes(self):
        """Получаем из json Python объект из которого будем забирать значения аттрибутов класса"""

        file = json.dumps(self.get_response(), indent=2, ensure_ascii=False)
        new_file = json.loads(file)
        return new_file
