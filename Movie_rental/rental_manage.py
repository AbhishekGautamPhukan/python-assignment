from catalog_manage import movies_available
from earning import add_earnings

movies_rented={}

def rent_movie(customer, title):
    for movie in movies_available:
        if movie[0] == title:
            movies_available.remove(movie)
            if customer in movies_rented:
                movies_rented[customer].append(movie)
            else:
                movies_rented[customer] = [movie]
            add_earnings(movie[2])
            print(f"'{title}' rented to {customer}.")
            return
    print(f"Movie '{title}' is not available.")
    
