import pytest
import logging
import WebsitesModules.Imdb as Imdb

logger:logging.Logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="log.log")

def test_RetriveMovieList():
    movielist:list[Imdb.ImdbSeachElement] = Imdb.searchMovieName("Stone")
    assert len(movielist) ==25
    
    
    
    
    
    
