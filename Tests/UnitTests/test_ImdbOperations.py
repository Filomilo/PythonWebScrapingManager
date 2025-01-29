from datetime import date, timedelta
import pytest
import logging
import WebsitesModules.Imdb as Imdb
import WebScraper as WebScraper
import Models.LanguageCodes as LanguageCodes

logger:logging.Logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="log.log")

def test_RetriveMovieList():
    movielist:list[Imdb.ImdbSeachElement] = Imdb.searchMovieName("Stone")
    assert len(movielist) ==25
    

def test_RetriveMovieDetailsFromUrl():
    data: Imdb.ImdbMediaInformation= Imdb.retriveMediaInformationByUrl("https://www.imdb.com/title/tt0111161/")
    assert data.title=="The Shawshank Redemption"
    assert data.rating==9.3
    assert data.releaseDate==date(year=1994, day=14,month=10)
    assert data.runtime==timedelta(hours=2, minutes=22)

def test_RetriveMovieDetailsInPolishFromUrl():
    webScraper: WebScraper.WebScraper= WebScraper.WebScraper()
    webScraper.defaultLangCode=LanguageCodes.LanguageCode.PL_PL
    data: Imdb.ImdbMediaInformation= Imdb.retriveMediaInformationByUrl("https://www.imdb.com/title/tt0111161/")
    assert data.title=="Skazani na Shawshank"
    assert data.rating==9.3
    assert data.releaseDate==date(year=1995, day=16,month=4)
    assert data.runtime==timedelta(hours=2, minutes=22)
    
    
    
    
