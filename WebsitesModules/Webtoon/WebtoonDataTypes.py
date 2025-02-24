from typing import List
import datetime

class WebtoonComicInfo:
    def __init__(self,
                 title:str,
                 author:str,
                 genre: List[str],
                 description: str,
                 views: str,
                 subscriptions: str,
                 grade: float,
                 comicPicUrl: str
                 ):
        self.title=title
        self.author=author
        self.genre=genre
        self.description=description
        self.views=views
        self.subscriptions=subscriptions
        self.grade=grade
        self.comicPicUrl=comicPicUrl

class WebtoonPageEntry:
    def __init__(self,
                 thumbnailUrl: str,
                 title: str,
                 date: datetime,
                 likes: int,
                 tx: int
                 ):
                 self.thumbnailUrl=thumbnailUrl
                 self.title=title
                 self.date=date
                 self.likes=likes
                 self.tx=tx

class WebtoonMainPageInfo:
    def __init__(self,
                 webtoonPageEntries: List[WebtoonPageEntry],
                 webtoonComicInfo: WebtoonComicInfo,
                 ):
                 self.webtoonPageEntries=webtoonPageEntries
                 self.webtoonComicInfo=webtoonComicInfo