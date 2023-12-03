import requests

#make an api call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:pythong+sort:stars+stars:>10000"