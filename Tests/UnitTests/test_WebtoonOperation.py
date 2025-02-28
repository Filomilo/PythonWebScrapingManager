from datetime import date, timedelta, datetime, timezone
import pytest
import logging
import WebsitesModules.Webtoon as Webtoon
import WebScraper as WebScraper
import Models.LanguageCodes as LanguageCodes
import WebsitesModules.Webtoon.WebtoonDataTypes as WebtoonDataTypes


logger:logging.Logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="log.log")

def test_RetriveWebcomicInfoByUrlEpicV():
    url: str="https://www.webtoons.com/en/comedy/epic-v/list?title_no=353"
    infoWebtoon: WebtoonDataTypes.WebtoonMainPageInfo= Webtoon.retiveComicPageInfo(url=url)
    assert infoWebtoon.webtoonComicInfo.title=="Epic V"
    assert infoWebtoon.webtoonComicInfo.author=="Ardtron, GNICE"
    assert infoWebtoon.webtoonComicInfo.genre==["Comedy"]
    assert infoWebtoon.webtoonComicInfo.description == "Epic V is a series about three friends, their snake, and epic V-necks. Sometimes our friends can be obnoxious, embarrassing, or nosy, but we accept them for who they are. Celebrate the awkward times of boyish friendship with Epic V!  "
    # assert infoWebtoon.webtoonComicInfo.views=='578,111' changes
    # assert infoWebtoon.webtoonComicInfo.subscriptions=='6,311' chnges
    assert infoWebtoon.webtoonComicInfo.grade==5.83
    assert infoWebtoon.webtoonPageEntries==[
        WebtoonDataTypes.WebtoonPageEntry(thumbnailUrl='', title='Ep. 27 (Last Episode)', date=datetime(2015, 3, 3, 0, 0, tzinfo=timezone.utc), likes=918, tx=27, url='https://www.webtoons.com/en/comedy/epic-v/ep-27-last-episode/viewer?title_no=353&episode_no=27'),
        WebtoonDataTypes.WebtoonPageEntry(thumbnailUrl='', title='Ep. 26', date=datetime(2015, 2, 26, 0, 0, tzinfo=timezone.utc), likes=753, tx=26, url='https://www.webtoons.com/en/comedy/epic-v/ep-26/viewer?title_no=353&episode_no=26'),
        WebtoonDataTypes.WebtoonPageEntry(thumbnailUrl='', title='Ep. 25', date=datetime(2015, 2, 24, 0, 0, tzinfo=timezone.utc), likes=641, tx=25, url='https://www.webtoons.com/en/comedy/epic-v/ep-25/viewer?title_no=353&episode_no=25'),
        WebtoonDataTypes.WebtoonPageEntry(thumbnailUrl='', title='Ep. 24', date=datetime(2015, 2, 19, 0, 0, tzinfo=timezone.utc), likes=780, tx=24, url='https://www.webtoons.com/en/comedy/epic-v/ep-24/viewer?title_no=353&episode_no=24'),
        WebtoonDataTypes.WebtoonPageEntry(thumbnailUrl='', title='Ep. 23', date=datetime(2015, 2, 17, 0, 0, tzinfo=timezone.utc), likes=625, tx=23, url='https://www.webtoons.com/en/comedy/epic-v/ep-23/viewer?title_no=353&episode_no=23'),
        WebtoonDataTypes.WebtoonPageEntry(thumbnailUrl='', title='Ep. 22', date=datetime(2015, 2, 12, 0, 0, tzinfo=timezone.utc), likes=709, tx=22, url='https://www.webtoons.com/en/comedy/epic-v/ep-22/viewer?title_no=353&episode_no=22'),
        WebtoonDataTypes.WebtoonPageEntry(thumbnailUrl='', title='Ep. 21', date=datetime(2015, 2, 10, 0, 0, tzinfo=timezone.utc), likes=750, tx=21, url='https://www.webtoons.com/en/comedy/epic-v/ep-21/viewer?title_no=353&episode_no=21'),
        WebtoonDataTypes.WebtoonPageEntry(thumbnailUrl='', title='Ep. 20', date=datetime(2015, 2, 5, 0, 0, tzinfo=timezone.utc), likes=700, tx=20, url='https://www.webtoons.com/en/comedy/epic-v/ep-20/viewer?title_no=353&episode_no=20'),
        WebtoonDataTypes.WebtoonPageEntry(thumbnailUrl='', title='Ep. 19', date=datetime(2015, 2, 3, 0, 0, tzinfo=timezone.utc), likes=808, tx=19, url='https://www.webtoons.com/en/comedy/epic-v/ep-19/viewer?title_no=353&episode_no=19'),
        WebtoonDataTypes.WebtoonPageEntry(thumbnailUrl='', title='Ep. 18', date=datetime(2015, 1, 29, 0, 0, tzinfo=timezone.utc), likes=731, tx=18, url='https://www.webtoons.com/en/comedy/epic-v/ep-18/viewer?title_no=353&episode_no=18')]

def test_RetriveWebcomicInfoByUrlWayward():
    url: str="https://www.webtoons.com/en/canvas/wayward/list?title_no=69342"
    infoWebtoon: WebtoonDataTypes.WebtoonMainPageInfo= Webtoon.retiveComicPageInfo(url=url)
    assert infoWebtoon.webtoonComicInfo.title=="Wayward"
    assert infoWebtoon.webtoonComicInfo.author=="SavvySnake"
    assert set( infoWebtoon.webtoonComicInfo.genre)==set( ["Fantasy","Comedy"])
    assert infoWebtoon.webtoonComicInfo.description  == "The one where everybody's dead - a silly little dark fantasy. | Tapas: tapas.io/series/ghoststory | Instagram: www.instagram.com/savvysnek | Twitter: https://twitter.com/savvysnek |"
    assert infoWebtoon.webtoonComicInfo.views=="5.2M"
    # assert infoWebtoon.webtoonComicInfo.subscriptions== "23,693" --- CHANGES TOO OFTEN
    assert infoWebtoon.webtoonComicInfo.grade==9.62