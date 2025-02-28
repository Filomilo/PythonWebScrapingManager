import urllib.parse
import logging
from PythonWebScrapingManager.WebScraper import WebScraper
from .FilmwebDataTypes import FilmwebSeachElement
from .FilmwebMediaDataExtraction import retriveMovieListFromHtmlSearchResult

logger: logging.Logger= logging.Logger(__name__)
webScraper: WebScraper= WebScraper()


# query=harry%20potter%20and%20the%20philosopher's%20stone


def _retrieveUrlSearchFilmweb(movieName: str) -> str:
    url = 'https://www.filmweb.pl/search#/?'
    params = {'query': movieName}
    encoded=url+urllib.parse.urlencode(params)
    return encoded

def searchMovieName(movieName: str)->list[FilmwebSeachElement]:
    urlToSearch:str= _retrieveUrlSearchFilmweb(movieName)
    htmlContent: str= webScraper.retriveHtmlFromUrlUsingWebDriver(url=urlToSearch,waitfor="sc-ehixzo kxLhCH")
    listOfMovies:list[FilmwebSeachElement]=  retriveMovieListFromHtmlSearchResult(htmlContent)
    logger.debug(f"retrives movies: {listOfMovies}")
    return listOfMovies
