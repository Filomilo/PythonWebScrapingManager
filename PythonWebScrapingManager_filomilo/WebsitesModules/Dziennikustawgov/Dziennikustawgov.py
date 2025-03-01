import logging

from bs4 import BeautifulSoup
from ...WebScraper import WebScraper
from .DziennikustawgovDataExtraction import ExtractListOfDocuments, extractPagesUrls
from  .DziennikustawgovDataTypes import DziennikustawgovDocument

logger: logging.Logger= logging.Logger(__name__)
webScraper: WebScraper= WebScraper()


def getDocumentsList(url: str)->list[DziennikustawgovDocument]:
    htmlContent: str = webScraper.retriveHtmlFromUrl(url=url)
    soup: BeautifulSoup = BeautifulSoup(htmlContent, "html.parser")
    listOfDocuments: list[DziennikustawgovDocument] = ExtractListOfDocuments(soup)
    return listOfDocuments

def getDocumentsListInWholeSection(url: str)->list[DziennikustawgovDocument]:
    htmlContent: str = webScraper.retriveHtmlFromUrl(url=url)
    soup: BeautifulSoup = BeautifulSoup(htmlContent, "html.parser")
    pageurls: list[str]=extractPagesUrls(soup)
    docs: list[DziennikustawgovDocument]=[]
    for pageurl in pageurls:
        docsTmp=getDocumentsList(pageurl)
        docs.extend(docsTmp)
    return docs
