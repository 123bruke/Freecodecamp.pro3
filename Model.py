from sklearn.neighbors import NearestNeighbors

def train_knn_model(sparse_matrix):

    model = NearestNeighbors(
        metric='cosine',
        algorithm='brute'
    )

    model.fit(sparse_matrix)
    return model
