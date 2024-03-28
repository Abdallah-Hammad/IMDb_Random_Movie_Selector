def getTitles(soup):
    movies = soup.select("a.ipc-title-link-wrapper")
    titles = []

    for movie in movies:
        titles.append(" ".join(movie.text.split()[1:]))

    titles = titles[:250]
    return titles


def getYears(soup):
    movies = soup.find_all(
        "span", class_="sc-b0691f29-8 ilsLEX cli-title-metadata-item"
    )

    years = []

    i = 0
    yearsList = list(range(1900, 2025))

    while i < 747:
        movie = movies[i].text
        try:
            movie = int(movie)
        except:
            pass
        if movie in yearsList:
            years.append(movie)
        i += 1

    return years


def getRatings(soup):
    movies = soup.find_all(
        "span",
        class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating",
    )

    ratings = []

    for movie in movies:
        rating = movie.text.split()
        ratings.append(rating[0])

    return ratings
