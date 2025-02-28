import pytest

from PythonWebScrapingManager import WebsitesModules as Filmweb


@pytest.mark.skip(reason="not yet implemented")
def test_RetriveMovieList():
    movielist:list[Filmweb.searchMovieName] = Filmweb.searchMovieName("Stone")
    assert len(movielist) ==25
    