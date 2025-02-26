from typing import List
import datetime
import attr

@attr.define
class WebtoonComicInfo:
    title:str
    author:str
    genre: List[str]
    description: str
    views: str
    subscriptions: str
    grade: float
    comicPicUrl: str

@attr.define
class WebtoonPageEntry:
    thumbnailUrl: str
    title: str
    date: datetime
    likes: int
    tx: int
    url: str


@attr.define
class WebtoonMainPageInfo:
    webtoonPageEntries: List[WebtoonPageEntry]
    webtoonComicInfo: WebtoonComicInfo