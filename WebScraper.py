
import urllib.parse
from bs4 import BeautifulSoup 
import requests

class WebScraper(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(WebScraper, cls).__new__(cls)
        return cls.instance
    
    def retriveHtmlFromUrl(self, url: str)->str:
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
        response : requests.Response = requests.get(url,headers=headers)
        if response.status_code != 200:
            raise BaseException(f"Couldn't reteive html from << {url} >> error code : <<{response.status_code}>>")
        return response.text
    




