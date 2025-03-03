from typing import List
from bs4 import BeautifulSoup
import logging

from ...WebScraper import WebScraper
from . import WebtoonsDataExtraction
from .WebtoonDataTypes import WebtoonMainPageInfo, WebtoonComicInfo, WebtoonPageEntry

logger: logging.Logger= logging.Logger(__name__)
webScraper: WebScraper= WebScraper()

def retiveComicPageInfo(url: str)->WebtoonMainPageInfo:
    htmlContent: str= webScraper.retriveHtmlFromUrl(url=url)
    soup:BeautifulSoup=BeautifulSoup(htmlContent,"html.parser")
    title:str= WebtoonsDataExtraction.extractTitle(soup)
    author:str= WebtoonsDataExtraction.extractAuthor(soup)
    genre: List[str]= WebtoonsDataExtraction.extractGenre(soup)
    description: str= WebtoonsDataExtraction.extractDescription(soup)
    views: str= WebtoonsDataExtraction.extractViews(soup)
    subscriptions: str= WebtoonsDataExtraction.extractSubscriptions(soup)
    grade: float= WebtoonsDataExtraction.extractGrade(soup)
    comicPicUrl: str= WebtoonsDataExtraction.extractComicPicUrl(soup)
    webtoonPageEntries: List[WebtoonPageEntry]= WebtoonsDataExtraction.extractPageEntries(soup)

    webtoonMainPageInfo:WebtoonMainPageInfo=WebtoonMainPageInfo(
            webtoonComicInfo=WebtoonComicInfo(
            title=title,
            author=author,
            genre=genre,
            description=description,
            views=views,
            subscriptions=subscriptions,
            grade=grade,
            comicPicUrl=comicPicUrl
        ),
        webtoonPageEntries=webtoonPageEntries

    )

    return webtoonMainPageInfo