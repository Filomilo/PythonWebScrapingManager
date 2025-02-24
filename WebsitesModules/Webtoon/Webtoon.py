from typing import Any, List
import urllib.parse
from bs4 import BeautifulSoup, ResultSet 
import requests
from datetime import date, timedelta
import logging
from WebScraper import WebScraper
from .WebtoonDataTypes import WebtoonMainPageInfo, WebtoonComicInfo
import WebsitesModules.Webtoon.WebtoonsDataExtraction as WebtoonsDataExtraction
logger: logging.Logger= logging.Logger(__name__)
webScraper: WebScraper= WebScraper()

def retiveComicPageInfo(url: str)->WebtoonMainPageInfo:
    htmlContent: str= webScraper.retriveHtmlFromUrl(url=url)
    soup:BeautifulSoup=BeautifulSoup(htmlContent,"html.parser")
    title:str=WebtoonsDataExtraction.extractTitle(soup)
    author:str=WebtoonsDataExtraction.extractAuthor(soup)
    genre: List[str]=[]
    description: str=""
    views: str=""
    subscriptions: str=""
    grade: float=0
    comicPicUrl: str=""
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
        webtoonPageEntries=[]

    )

    return webtoonMainPageInfo
    # 
    # 
    # imdbMediaInformation: ImdbMediaInformation=ImdbMediaInformation()
    # imdbMediaInformation.title= extractTileFromPage(soup)
    # imdbMediaInformation.rating=extractRatingFromPage(soup)
    # imdbMediaInformation.releaseDate=extractReleaseDateFromPage(soup)
    # imdbMediaInformation.runtime=extractRunTimeFromPage(soup)
    # return imdbMediaInformation