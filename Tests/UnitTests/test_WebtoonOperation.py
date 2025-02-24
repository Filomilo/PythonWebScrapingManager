from datetime import date, timedelta
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
    

def test_RetriveWebcomicInfoByUrlWayward():
    url: str="https://www.webtoons.com/en/canvas/wayward/list?title_no=69342"
    infoWebtoon: WebtoonDataTypes.WebtoonMainPageInfo= Webtoon.retiveComicPageInfo(url=url)
    assert infoWebtoon.webtoonComicInfo.title=="Wayward"

