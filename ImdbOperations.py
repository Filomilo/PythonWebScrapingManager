import urllib.parse
from bs4 import BeautifulSoup 
import requests

class ImdbInformation:
    name: str
    def __init__(name):
        self.name=name


def retrieveUrlSearchImdb(movieName: str) -> str:
    encoded_name = urllib.parse.quote(movieName)
    return f"https://www.imdb.com/find/?q={encoded_name}"

def retriveImdbInfo(movieName:str)-> ImdbInformation:
    url:str=retrieveUrlSearchImdb(movieName)
    SearchPage : requests.Response = requests.get(url)
    if SearchPage.status_code != 200:
        raise BaseException(f"Couldn't reteive imdb search information for {movieName}, error: {SearchPage.status_code}-{SearchPage.content}")
    SearchPageSoup:BeautifulSoup = BeautifulSoup(SearchPage.text, 'html.parser')
    print(SearchPageSoup.contents)