from typing import Any
from bs4 import BeautifulSoup, ResultSet, Tag
def extractTitle(soup: BeautifulSoup)-> str:
    try:
        info= soup.find("div",attrs={'class': 'info'})
        titleElement=info.find(attrs={'class': 'subj'})
        title:str=titleElement.contents[0]
        title=title.replace("\t", "").replace("\n", "")
        return title
    except BaseException as ex:
        return f"error getting author : [{ex}]"

def extractAuthor(soup: BeautifulSoup)-> str:
    return ""
    pass
    # try:
    #     info= soup.find("div",attrs={'class': 'info'})
    #     titleElement=info.find(attrs={'class': 'subj'})
    #     title:str=titleElement.contents[0]
    #     title=title.replace("\t", "").replace("\n", "")
    #     return title
    # except BaseException as ex:
    #     return f"error getting author : [{ex}]"


    # print(html_content)
    # soup:BeautifulSoup = BeautifulSoup(html_content, 'html.parser')
    # htmlSerachResultElements:ResultSet[Any]= soup.find_all("li", attrs={'class': 'sc-ehixzo kxLhCH'})
    # moveList: list[FilmwebSeachElement]=[getFilmwebSeachElementFromHtmlElement(x) for x in htmlSerachResultElements]
    # return moveList