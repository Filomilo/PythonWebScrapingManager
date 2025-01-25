import  WebsitesModules.Filmweb as Filmweb


def test_RetriveMovieList():
    movielist:list[Filmweb.searchMovieName] = Filmweb.searchMovieName("Stone")
    assert len(movielist) ==25
    