import random
import requests
from bs4 import BeautifulSoup
from info import getTitles, getYears, getRatings

url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def main():
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    movieTitles = getTitles(soup)
    movieYears = getYears(soup)
    movieRatings = getRatings(soup)

    while(True):
        id = random.randrange(0, len(movieTitles))
        print(f'{movieTitles[id]}, {movieYears[id]}, rating: {movieRatings[id]}')
        
        go_on = input("Do you want another movie [y/n] ? ")
        
        if go_on != 'y':
            break

if __name__ == "__main__":
    main()
