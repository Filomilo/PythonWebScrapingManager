from datetime import datetime, timezone

from PythonWebScrapingManager_filomilo.WebsitesModules.Dziennikustawgov import Dziennikustawgov
from PythonWebScrapingManager_filomilo.WebsitesModules.Dziennikustawgov.DziennikustawgovDataTypes import \
    DziennikustawgovDocument


def test_documentRerival():
    url:str="https://dziennikustaw.gov.pl/DU/rok/2012"
    documentsRecevied: list[DziennikustawgovDocument]= Dziennikustawgov.getDocumentsList(url)
    assert len(documentsRecevied)>0
    assert documentsRecevied==[
        DziennikustawgovDocument(
                                  title='Wyrok Trybunału Konstytucyjnego z dnia 19 grudnia 2012 r. sygn. akt K 9/12',
                                  pdfUrl='https://dziennikustaw.gov.pl/DU/2012/1555/D2012000155501.pdf',
                                  date=datetime(2012, 12, 31, 0, 0, tzinfo=timezone.utc),
                                  position=1555
                                  ),
         DziennikustawgovDocument(
                                  title='Wyrok Trybunału Konstytucyjnego z dnia 20 grudnia 2012 r. sygn. akt K 28/11',
                                  pdfUrl='https://dziennikustaw.gov.pl/DU/2012/1554/D2012000155401.pdf',
                                  date=datetime(2012, 12, 31, 0, 0, tzinfo=timezone.utc),
                                  position=1554
                                  ),
         DziennikustawgovDocument(
                                 title='Rozporządzenie Prezesa Rady Ministrów z dnia 21 grudnia 2012 r. w sprawie przedterminowych wyborów wójta gminy Zawonia w województwie dolnośląskim',
                                 pdfUrl='https://dziennikustaw.gov.pl/DU/2012/1553/D2012000155301.pdf',
                                 date=datetime(2012, 12, 31, 0, 0, tzinfo=timezone.utc),
                                 position=1553
         ),
         DziennikustawgovDocument(
                                 title='Rozporządzenie Prezesa Rady Ministrów z dnia 21 grudnia 2012 r. w sprawie przedterminowych wyborów burmistrza Raciąża w województwie mazowieckim',
                                 pdfUrl='https://dziennikustaw.gov.pl/DU/2012/1552/D2012000155201.pdf',
                                 date=datetime(2012, 12, 31, 0, 0, tzinfo=timezone.utc),
                                 position=1552
         ),
         DziennikustawgovDocument(
                                 title='Ustawa z dnia 9 listopada 2012 r. o umorzeniu należności powstałych z tytułu nieopłaconych składek przez osoby prowadzące pozarolniczą działalność',
                                 pdfUrl='https://dziennikustaw.gov.pl/DU/2012/1551/D2012000155101.pdf',
                                 date=datetime(2012, 12, 31, 0, 0, tzinfo=timezone.utc),
                                 position=1551)]


def test_documentFromSectionRetrival():
    url:str="https://dziennikustaw.gov.pl/DU/rok/2012"
    documentsRecevied: list[DziennikustawgovDocument]= Dziennikustawgov.getDocumentsListInWholeSection(url)
    assert len(documentsRecevied)==1555