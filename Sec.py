from src.data_preprocessing import clean_ratings
from src.model import train_knn_model
from src.recommender import get_recommends
from src.utils import create_sparse_matrix

# Clean data
ratings_clean = clean_ratings(ratings)

# Create pivot table
book_user_table = ratings_clean.pivot_table(
    index='isbn',
    columns='user_id',
    values='rating'
).fillna(0)

# Train model
book_sparse = create_sparse_matrix(book_user_table)
knn_model = train_knn_model(book_sparse)
