import json
from src.mixin import APIMixin


class Channel(APIMixin):
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = self.get_attributes()['items'][0]['snippet']['title']
        self.description = self.get_attributes()['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscriber_count = self.get_attributes()['items'][0]['statistics']['subscriberCount']
        self.video_count = self.get_attributes()['items'][0]['statistics']['videoCount']
        self.view_count = self.get_attributes()['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title}'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)

    def get_response(self):
        request = self.get_service().channels().list(
            part="snippet,contentDetails,statistics",
            id=self.__channel_id
        )
        response = request.execute()

        return response

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(Channel.get_response(self), indent=2, ensure_ascii=False))

    def get_attributes(self):
        """Получаем из json Python объект из которого будем забирать значения аттрибутов класса"""

        file = json.dumps(Channel.get_response(self), indent=2, ensure_ascii=False)
        new_file = json.loads(file)
        return new_file

    @property
    def channel_id(self):
        """Делаем аттрибут channel_id защищенным"""

        return self.__channel_id

    def to_json(self, file):
        """Функция для записи аттрибутов класса в json файл"""

        attributes = {}
        attributes['channel_id'] = self.__channel_id
        attributes['title'] = self.title
        attributes['description'] = self.description
        attributes['url'] = self.url
        attributes['subscriber_count'] = self.subscriber_count
        attributes['video_count'] = self.video_count
        attributes['view_count'] = self.view_count
        with open(file, 'w') as f:
            json.dump(attributes, f)
