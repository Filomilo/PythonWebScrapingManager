import pytest

from PythonWebScrapingManager_filomilo.WebsitesModules.Filmweb import Filmweb


@pytest.mark.skip(reason="not yet implemented")
def test_RetriveMovieList():
    movielist:list[Filmweb.searchMovieName] = Filmweb.searchMovieName("Stone")
    assert len(movielist) ==25
    