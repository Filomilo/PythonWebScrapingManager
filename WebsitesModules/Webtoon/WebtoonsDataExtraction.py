from dataclasses import replace
from datetime import datetime, timezone
from typing import Any, List
from bs4 import BeautifulSoup, ResultSet, Tag

from zoneinfo import ZoneInfo
from selenium.webdriver.support.expected_conditions import none_of

from .WebtoonDataTypes import WebtoonPageEntry
def extractTitle(soup: BeautifulSoup)-> str:
    try:
        info= soup.find("div",attrs={'class': 'info'})
        titleElement=info.find(attrs={'class': 'subj'})
        title:str=titleElement.get_text()
        title=title.replace("\t", "").replace("\n", "")
        return title
    except BaseException as ex:
        return f"error getting title : [{ex}]"

def extractAuthor(soup: BeautifulSoup)-> str:
    try:
        authorelement:Tag= soup.find("a",attrs={'class': 'author'})
        if authorelement is None:
            authorelement=soup.find(attrs={'class': 'author_area'})
        if authorelement is None:
            raise BaseException("Couldn't find author element")
        author=authorelement \
                .get_text(strip=True) \
                .replace("\n","") \
                .replace("\t","") \
                .replace("author info","" )
        return author
    except BaseException as ex:
        return f"error getting author : [{ex}]"

def extractGenre(soup: BeautifulSoup)-> List[str]:
    try:
        genresElements: []= soup.find_all('h2',attrs={'class': 'genre'})
        genres= [x.get_text(strip=True) for x in genresElements]
        return genres 
    except BaseException as ex:
        return f"error getting genras : [{ex}]"
    
def extractDescription(soup: BeautifulSoup)-> str:
    try:
        summaryElement:Tag=soup.find(attrs={'class': 'summary'})
        summaryText: str=summaryElement.getText()
        return summaryText 
    except BaseException as ex:
        return f"error getting description : [{ex}]"
    
def extractViews(soup: BeautifulSoup)-> str:
    try:
        gradeArea:Tag=soup.find(attrs={'class': 'grade_area'})
        countElements: ResultSet[Tag]=gradeArea.find_all(attrs={'class': 'cnt'})
        viewsVal:str=countElements[0].getText()
        return viewsVal
    except BaseException as ex:
        return f"error getting Views : [{ex}]"

def extractSubscriptions(soup: BeautifulSoup)-> str:
    try:
        gradeArea:Tag=soup.find(attrs={'class': 'grade_area'})
        countElements: ResultSet[Tag]=gradeArea.find_all(attrs={'class': 'cnt'})
        subsVal:str=countElements[1].getText()
        return subsVal
    except BaseException as ex:
        return f"error getting Subscriptions : [{ex}]"
    
def extractGrade(soup: BeautifulSoup)-> float:
    try:
        gradeArea:Tag=soup.find(attrs={'class': 'grade_area'})
        countElements: ResultSet[Tag]=gradeArea.find_all(attrs={'class': 'cnt'})
        gradestr:str=countElements[2].getText()
        return float(gradestr)
    except BaseException as ex:
        return -1

    
def extractComicPicUrl(soup: BeautifulSoup)-> str:
    try:
        thubnailElementSrc:str=soup \
        .find(attrs={'class': 'detail_header challenge'}) \
        .find('img') \
        ['src']
        return thubnailElementSrc
    except BaseException as ex:
        return f"error getting thumbnail : [{ex}]"

def extractPageEntries(soup: BeautifulSoup)-> List[WebtoonPageEntry]:
    try:
        entiresTags: ResultSet[Tag]=soup.find_all(attrs={'class':'_episodeItem'})
        entires: List[WebtoonPageEntry]= [extractPageEntry(x) for x in entiresTags]
        return entires
    except BaseException as ex:
        return []
def extractPageEntry(soup: BeautifulSoup)-> WebtoonPageEntry:
    try:
        href:str=soup.find("a")['href']
        date_str = soup.find(attrs={'class': 'date'}).get_text().replace("\n","").replace("\t","")
        date = datetime.strptime(date_str, "%b %d, %Y")
        date=date.replace(tzinfo=timezone.utc)
        return WebtoonPageEntry(
            thumbnailUrl="",
            title=soup.find("span",attrs={'class': 'subj'}).get_text(),
            date=date,
            likes= int (soup.find('span',attrs={'class': 'like_area'}).get_text(strip=True).replace('like','').replace(",","")),
            tx=int(soup.find('span',attrs={'class': 'tx'}).get_text().replace('#','')),
            url=href
        )
    except BaseException as ex:
        return WebtoonPageEntry(url="",thumbnailUrl="",title=f"ERROR: [{ex}]",date=datetime(day=1,month=1,year=1900),likes=-1,tx=-1)

