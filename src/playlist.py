from datetime import timedelta
from src.channel import Channel
import isodate


class PlayList(Channel):
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.title = self.get_response_playlist()['items'][0]['snippet']['title'][:24]
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    def get_response_playlist(self):
        """Получаем статистику видео по его id"""

        playlist_videos = super().get_service().playlistItems().list(playlistId=self.playlist_id,
                                                                     part='snippet,contentDetails',
                                                                     maxResults=50,
                                                                     ).execute()
        return playlist_videos

    @property
    def total_duration(self):
        """Метод возвращает суммарную длительность всех видео плейлиста"""

        total = timedelta(hours=0, minutes=0, seconds=0)
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.get_response_playlist()['items']]
        video_response = super().get_service().videos().list(part='contentDetails,statistics',
                                                             id=','.join(video_ids)
                                                             ).execute()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)

            total += duration
        return total

    def show_best_video(self):
        """Метод возвращает ссылку на самое популярное видео"""

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.get_response_playlist()['items']]
        video_response = super().get_service().videos().list(part='contentDetails,statistics',
                                                             id=','.join(video_ids)
                                                             ).execute()
        likes = []
        for video in video_response['items']:
            likes.append(video['statistics']['likeCount'])
        best = max(likes)
        for video in video_response['items']:
            if video['statistics']['likeCount'] == best:
                return f'https://youtu.be/{video['id']}'
