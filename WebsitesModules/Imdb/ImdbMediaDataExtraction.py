from datetime import datetime, timedelta
from sqlite3 import Date
from bs4 import BeautifulSoup


def extractTileFromPage(html: BeautifulSoup)-> str:
    titleElement:BeautifulSoup=html.find(attrs={"class":"hero__primary-text"})
    title:str=titleElement.contents[0]
    return title

def extractRatingFromPage(html: BeautifulSoup)-> float:
    RatingElement:BeautifulSoup=html.find(attrs={"data-testid":"hero-rating-bar__aggregate-rating__score"})
    rating:str=RatingElement.contents[0].contents[0]
    return float(rating)


def extractReleaseDateFromPage(html: BeautifulSoup)-> Date:
    relaseDateElement:BeautifulSoup=html.find(attrs={"data-testid":"title-details-releasedate"})
    dateElement=relaseDateElement.find(attrs={"class":"ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})
    dateString:str=dateElement.contents[0]
    datesplit: list[str]=dateString.replace(',', '').split(" ")
    mothNumber: int=datetime.strptime(datesplit[0], "%B").month
    dayNumber:int=int(datesplit[1])
    yearNumber: int=int(datesplit[2])
    return Date(year=yearNumber,day=dayNumber,month=mothNumber)


def extractRunTimeFromPage(html: BeautifulSoup)-> timedelta:
    runtimeElement:BeautifulSoup=html.find(attrs={"data-testid":"title-techspec_runtime"})
    runTimeString:str=runtimeElement.find(attrs={"class":"ipc-metadata-list-item__content-container"}).text
    splits:list[str]=runTimeString.split()
    indexOfMinuts:int=splits.index("minutes")
    indexOfHours:int=splits.index("hours")
    hour:int=int(splits[indexOfHours-1])
    minuts:int=int(splits[indexOfMinuts-1])
    return timedelta(minutes=minuts, hours=hour)