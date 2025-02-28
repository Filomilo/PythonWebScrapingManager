from datetime import datetime, timezone


from bs4 import BeautifulSoup, Tag, ResultSet

from WebsitesModules.Dziennikustawgov.DziennikustawgovDataTypes import DziennikustawgovDocument


def ExtractListOfDocuments(soup: BeautifulSoup)->list[DziennikustawgovDocument]:
    tableBody=soup.find('tbody')
    tableElements = tableBody.find_all('tr')
    test1=tableElements[0].get("class")
    test2 = tableElements[3].get("class")
    tableElementsFiltered=[tr for tr in tableElements if tr.get("class" ) is None ]
    listOFDocuments:list[DziennikustawgovDocument] = [extractSigngleDocuments(x) for x in tableElementsFiltered]
    return listOFDocuments

def extractSigngleDocuments(soup: BeautifulSoup)->DziennikustawgovDocument:
    tds=soup.find_all('td')
    positonStr:str=tds[0].get_text().replace('\n','').replace('\t','').replace('\r','')
    dateStr=tds[3].get_text().replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    titleStr:str=tds[1].get_text().replace('\n','').replace('\t','').replace('\r','')
    pdfUrlStr:str="https://dziennikustaw.gov.pl"+tds[2].find("a")['href'].replace('\n','').replace('\t','').replace('\r','')
    return DziennikustawgovDocument(
        position= int(positonStr),
        title=titleStr,
        pdfUrl=pdfUrlStr,
        date=datetime.strptime(dateStr, "%Y-%m-%d")
    )
