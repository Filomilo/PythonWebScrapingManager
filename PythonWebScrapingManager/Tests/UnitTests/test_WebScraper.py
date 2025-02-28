import pytest
import logging
from PythonWebScrapingManager.WebScraper import WebScraper
logger:logging.Logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="log.log")
def test_singleton():
    obj1: WebScraper= WebScraper()
    obj2: WebScraper=WebScraper()
    assert obj1 is obj2


webScraper: WebScraper= WebScraper()
UrlRetivlasTest: list[str]=[
    "https://www.imdb.com/find/?q=object",
    "https://www.imdb.com/find/?q=none",
    "https://www.rottentomatoes.com/m/flow_2024"
]
@pytest.mark.parametrize("url", UrlRetivlasTest)
def test_retriveHtml(url: str):
    content:str=webScraper.retriveHtmlFromUrl(url)
    print(content)

    
    
    
    
