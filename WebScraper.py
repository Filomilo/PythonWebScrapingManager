
from typing import Optional
import urllib.parse
from bs4 import BeautifulSoup 
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class WebScraper(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(WebScraper, cls).__new__(cls)
        return cls.instance
    
    def retriveHtmlFromUrl(self, url: str)->str:
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US"
    }
        response : requests.Response = requests.get(url,headers=headers)
        if response.status_code != 200:
            raise BaseException(f"Couldn't reteive html from << {url} >> error code : <<{response.status_code}>>")
        return response.text
    

    def retriveHtmlFromUrlUsingWebDriver(self, url: str, waitfor: Optional[str])->str:
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        if waitfor is not None:
            wait = WebDriverWait(driver, 20)
            element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, waitfor)))

        page_source = driver.page_source
        return page_source
    




