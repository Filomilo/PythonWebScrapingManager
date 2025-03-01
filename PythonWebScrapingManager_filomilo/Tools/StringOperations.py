
def cleanUpWhiteCharacters(string:str)->str:
    return string.replace('\n','').replace('\t','').replace('\r','')