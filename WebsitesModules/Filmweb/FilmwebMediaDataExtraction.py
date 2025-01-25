from typing import Any
from bs4 import BeautifulSoup, ResultSet
from .FilmwebDataTypes import FilmwebSeachElement


def  getFilmwebSeachElementFromHtmlElement(content: BeautifulSoup)->FilmwebSeachElement:
    return "null"

def retriveMovieListFromHtmlSearchResult(html_content: str)-> list[FilmwebSeachElement]:
    print(html_content)
    soup:BeautifulSoup = BeautifulSoup(html_content, 'html.parser')
    htmlSerachResultElements:ResultSet[Any]= soup.find_all("li", attrs={'class': 'sc-ehixzo kxLhCH'})
    moveList: list[FilmwebSeachElement]=[getFilmwebSeachElementFromHtmlElement(x) for x in htmlSerachResultElements]
    return moveList