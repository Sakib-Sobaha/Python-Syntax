from fastapi import FastAPI, HTTPException, Query
import json
from pathlib import Path

app = FastAPI(title="MovieHub API")

DATA_PATH = Path(__file__).parent / "data.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

movies = data["movies"]
users = data["users"]
directors = data["directors"]
reviews = data["reviews"]

@app.get("/movies")
def get_movies():
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: str):
    for m in movies:
        if m["id"] == movie_id:
            return m
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: str):
    for u in users:
        if u["id"] == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/sortedRating")
def get_sorted_rating():
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return sorted_movies


# --- Interview problem-solving endpoints (use JSON data) ---

@app.get("/movies/top")
def get_top_movies(limit: int = Query(5, ge=1, le=50)):
    """Top N movies by rating; ties broken by ratingCount descending."""
    sorted_movies = sorted(
        movies,
        key=lambda m: (m["rating"], m["ratingCount"]),
        reverse=True,
    )
    return sorted_movies[:limit]


@app.get("/directors/{director_id}/movies")
def get_director_movies(director_id: str):
    """All movies by a given director."""
    director = next((d for d in directors if d["id"] == director_id), None)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    result = [m for m in movies if m["directorId"] == director_id]
    return {"director": director, "movies": result}


@app.get("/movies/{movie_id}/reviews")
def get_movie_reviews(movie_id: str):
    """All reviews for a movie; 404 if movie not found."""
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    result = [r for r in reviews if r["movieId"] == movie_id]
    return {"movie": movie, "reviews": result}


@app.get("/genres/{genre}/movies")
def get_movies_by_genre(genre: str):
    """Filter movies by genre (case-insensitive)."""
    genre_lower = genre.strip().lower()
    result = [m for m in movies if m["genre"].lower() == genre_lower]
    return {"genre": genre, "movies": result, "count": len(result)}


@app.get("/movies/search")
def search_movies(q: str = Query(..., min_length=1)):
    """Search movies by title (substring, case-insensitive)."""
    q_lower = q.strip().lower()
    result = [m for m in movies if q_lower in m["title"].lower()]
    return {"query": q, "movies": result, "count": len(result)}


@app.get("/stats/summary")
def get_stats_summary():
    """Aggregate stats: total movies, avg rating, count per genre."""
    total = len(movies)
    avg_rating = round(sum(m["rating"] for m in movies) / total, 2) if total else 0
    genre_counts = {}
    for m in movies:
        g = m["genre"]
        genre_counts[g] = genre_counts.get(g, 0) + 1
    return {
        "totalMovies": total,
        "averageRating": avg_rating,
        "moviesPerGenre": genre_counts,
        "totalUsers": len(users),
        "totalReviews": len(reviews),
    }


@app.get("/movies/highest-rated")
def get_highest_rated():
    """Single highest-rated movie; if tie, the one with more ratingCount."""
    if not movies:
        raise HTTPException(status_code=404, detail="No movies")
    best = max(movies, key=lambda m: (m["rating"], m["ratingCount"]))
    return best


@app.get("/users/{user_id}/reviews")
def get_user_reviews(user_id: str):
    """All reviews written by a user."""
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    result = [r for r in reviews if r["userId"] == user_id]
    return {"user": user, "reviews": result}


@app.get("/directors/top-by-movie-count")
def get_directors_by_movie_count():
    """Directors sorted by number of movies (desc), then by name."""
    counts = {}
    for m in movies:
        did = m["directorId"]
        counts[did] = counts.get(did, 0) + 1
    director_list = [
        {"id": d["id"], "name": d["name"], "movieCount": counts.get(d["id"], 0)}
        for d in directors
    ]
    director_list.sort(key=lambda x: (-x["movieCount"], x["name"]))
    return director_list


@app.get("/movies/year-range")
def get_movies_year_range(
    min_year: int = Query(None),
    max_year: int = Query(None),
):
    """Movies in optional year range (inclusive)."""
    result = movies
    if min_year is not None:
        result = [m for m in result if m["year"] >= min_year]
    if max_year is not None:
        result = [m for m in result if m["year"] <= max_year]
    result = sorted(result, key=lambda m: m["year"])
    return {"movies": result, "count": len(result)}


@app.get("/reviews/average-by-movie")
def get_average_review_by_movie():
    """Average review score per movie (from reviews JSON only)."""
    by_movie = {}
    for r in reviews:
        mid = r["movieId"]
        if mid not in by_movie:
            by_movie[mid] = []
        by_movie[mid].append(r["score"])
    result = [
        {
            "movieId": mid,
            "averageScore": round(sum(scores) / len(scores), 2),
            "reviewCount": len(scores),
        }
        for mid, scores in by_movie.items()
    ]
    result.sort(key=lambda x: -x["averageScore"])
    return result


@app.get("/movies/with-review-count")
def get_movies_with_review_count():
    """All movies with count of reviews from reviews array."""
    review_counts = {}
    for r in reviews:
        mid = r["movieId"]
        review_counts[mid] = review_counts.get(mid, 0) + 1
    result = []
    for m in movies:
        result.append({
            **m,
            "reviewCount": review_counts.get(m["id"], 0),
        })
    result.sort(key=lambda x: -x["reviewCount"])
    return result
