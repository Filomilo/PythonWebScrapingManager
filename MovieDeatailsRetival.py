import typing
from ImdbOperations import *

def readMoviesFromFile(fileDir: str)->list[str]:
    lines: list[str]
    with open(fileDir, 'r') as file:
        lines = file.readlines()
    return lines


movies=readMoviesFromFile("MoviesToRetrive.txt")
# print(movies)
for file in movies:
    print(file)
    ImdbInfo:ImdbInformation= retriveImdbInfo(file)
    

