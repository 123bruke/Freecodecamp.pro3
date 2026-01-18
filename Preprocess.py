import pandas as pd

def clean_ratings(ratings, min_user_ratings=200, min_book_ratings=100):
    active_users = ratings['user_id'].value_counts()
    popular_books = ratings['isbn'].value_counts()

    cleaned_ratings = ratings[
        ratings['user_id'].isin(active_users[active_users >= min_user_ratings].index) &
        ratings['isbn'].isin(popular_books[popular_books >= min_book_ratings].index)
    ]

    return cleaned_ratings
