from datetime import datetime, timezone


from bs4 import BeautifulSoup, ResultSet, Tag, PageElement, NavigableString

from .DziennikustawgovDataTypes import DziennikustawgovDocument
from ...Tools.StringOperations import cleanUpWhiteCharacters


def ExtractListOfDocuments(soup: BeautifulSoup)->list[DziennikustawgovDocument]:
    tableBody=soup.find('tbody')
    tableElements = tableBody.find_all('tr')
    headers=extractTableHeaders(soup)
    tableElementsFiltered=[tr for tr in tableElements if tr.get("class" ) is None ]
    listOFDocuments:list[DziennikustawgovDocument] = [extractSigngleDocuments(x,
                                                                              postionIndex=headers.index("Pozycja"),
                                                                              dateIndex=headers.index("Data ogłoszenia"),
                                                                              titleIndex=headers.index('Tytuł'),
                                                                              pdfUrlIndex=headers.index("Pliki")
                                                                              ) for x in tableElementsFiltered]
    return listOFDocuments

def extractTableHeaders(soup: BeautifulSoup)->list[str]:
    ths: ResultSet = soup.find_all('th')
    headers: list[str] = [th.get_text().strip() for th in ths]
    return headers

def extractSigngleDocuments(soup: BeautifulSoup,
                            postionIndex: int=0,
                            dateIndex: int=3,
                            titleIndex: int=1,
                            pdfUrlIndex: int=2
                            )->DziennikustawgovDocument:
    tds=soup.find_all('td')




    positonStr:str=cleanUpWhiteCharacters(tds[postionIndex].get_text())
    dateStr=tds[dateIndex].get_text().replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    titleStr:str=tds[titleIndex].get_text().replace('\n','').replace('\t','').replace('\r','')
    pdfUrlStr:str="https://dziennikustaw.gov.pl"+tds[pdfUrlIndex].find("a")['href'].replace('\n','').replace('\t','').replace('\r','')
    return DziennikustawgovDocument(
        position= int(positonStr),
        title=titleStr,
        pdfUrl=pdfUrlStr,
        date=datetime.strptime(dateStr, "%Y-%m-%d").replace(tzinfo=timezone.utc)

    )
def extractPagesUrls(soup:BeautifulSoup)->list[str]:
    pagesSection:BeautifulSoup=soup.find('div',attrs={'class':'frigth'})
    aElmenents: ResultSet = pagesSection.find_all('a')
    urls: list[str]= ["https://dziennikustaw.gov.pl"+x['href'] for x in aElmenents]
    return urls