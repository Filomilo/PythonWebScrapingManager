from typing import Any
import urllib.parse
from bs4 import BeautifulSoup, ResultSet
from datetime import date, timedelta
import logging

from ...WebScraper import  WebScraper
from .ImdbMediaDataExtraction import extractTileFromPage, extractRatingFromPage, \
    extractReleaseDateFromPage, extractRunTimeFromPage

logger: logging.Logger= logging.Logger(__name__)
webScraper: WebScraper= WebScraper()

class ImdbMediaInformation:
    title: str
    releaseDate: date
    rating: float
    runtime: timedelta
    def __init__(self,):
        pass

class ImdbSeachElement:
    def __init__(self,title,href):
        self.title=title
        self.href=href


def _retrieveUrlSearchImdb(movieName: str) -> str:
    url = 'https://www.imdb.com/find/?'
    params = {'q': movieName,"s":"tt"}
    encoded=url+urllib.parse.urlencode(params)
    return encoded

def getImdbSeachElementFromHtmlElement(htmlElement:BeautifulSoup)->ImdbSeachElement:
    titleElement:BeautifulSoup = htmlElement.find(attrs={"class": "ipc-metadata-list-summary-item__t"})
    title:str=titleElement.contents[0]
    href:str=titleElement["href"]
    return ImdbSeachElement(title=title,href=href)

def retriveMovieListFromHtmlSearchResult(html_content: str)-> list[ImdbSeachElement]:
    print(html_content)
    soup:BeautifulSoup = BeautifulSoup(html_content, 'html.parser')
    htmlSerachResultElements:ResultSet[Any]= soup.find_all(attrs={'class': 'find-title-result'})
    moveList: list[ImdbSeachElement]=[getImdbSeachElementFromHtmlElement(x) for x in htmlSerachResultElements]
    return moveList


def searchMovieName(movieName: str)->list[ImdbSeachElement]:
    urlToSearch:str= _retrieveUrlSearchImdb(movieName)
    htmlContent: str= webScraper.retriveHtmlFromUrl(url=urlToSearch)
    listOfMovies:list[ImdbSeachElement]=  retriveMovieListFromHtmlSearchResult(htmlContent)
    logger.debug(f"retrives movies: {listOfMovies}")
    return listOfMovies

def retriveMediaInformaionByUrl(url: str)->ImdbMediaInformation:
    htmlContent: str= webScraper.retriveHtmlFromUrl(url=url)
    soup:BeautifulSoup=BeautifulSoup(htmlContent,"html.parser")
    imdbMediaInformation: ImdbMediaInformation=ImdbMediaInformation()
    imdbMediaInformation.title= extractTileFromPage(soup)
    imdbMediaInformation.rating=extractRatingFromPage(soup)
    imdbMediaInformation.releaseDate=extractReleaseDateFromPage(soup)
    imdbMediaInformation.runtime=extractRunTimeFromPage(soup)
    return imdbMediaInformation


def retriveMediaInformationByUrl(serachby: str|ImdbSeachElement)->ImdbMediaInformation:
    if isinstance(serachby,str):
        return retriveMediaInformaionByUrl(serachby)
    raise ValueError("Wrong argument")


