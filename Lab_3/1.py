def high_imdb(movie):
    imdb = movie["imdb"] > 5.5
    return imdb

movie = {
    "name": "Usual Suspects", 
    "imdb": 7.0,
    "category": "Thriller"
}

print(high_imdb(movie)) 