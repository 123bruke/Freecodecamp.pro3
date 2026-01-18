def get_recommends(book_title, books, book_user_table, model, n_recommendations=5):

    book_isbn = books.loc[
        books['title'] == book_title, 'isbn'
    ].values[0]

    book_index = book_user_table.index.get_loc(book_isbn)

    distances, indices = model.kneighbors(
        book_user_table.iloc[book_index].values.reshape(1, -1),
        n_neighbors=n_recommendations + 1
    )

    recommendations = []

    for i in range(1, len(distances.flatten())):
        neighbor_isbn = book_user_table.index[indices.flatten()[i]]
        neighbor_title = books.loc[
            books['isbn'] == neighbor_isbn, 'title'
        ].values[0]

        recommendations.append([
            neighbor_title,
            distances.flatten()[i]
        ])

    return [book_title, recommendations]
