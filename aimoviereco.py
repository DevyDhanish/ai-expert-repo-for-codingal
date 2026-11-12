
movies = {
    "Interstellar": ["Sci-Fi", "Adventure", "Drama"],
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Avengers": ["Action", "Sci-Fi", "Adventure"],
    "Titanic": ["Romance", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "The Conjuring": ["Horror", "Thriller"],
    "IT": ["Horror", "Thriller"],
    "Joker": ["Crime", "Drama", "Thriller"],
    "Avatar": ["Sci-Fi", "Adventure", "Fantasy"]
}

def recommend_movie(movie_name):
    if movie_name not in movies:
        print("Movie not found!")
        return

    selected_genres = set(movies[movie_name])
    recommendations = []

    for movie, genres in movies.items():

        if movie == movie_name:
            continue

        common = selected_genres.intersection(genres)

        score = len(common) / len(selected_genres.union(genres))

        recommendations.append((movie, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:")

    for movie, score in recommendations[:3]:
        print(f"{movie} - Match: {score * 100:.1f}%")


print("Available Movies:")
for movie in movies:
    print("-", movie)

choice = input("\nEnter a movie you like: ")

recommend_movie(choice)
