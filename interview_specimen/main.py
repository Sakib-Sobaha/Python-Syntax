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
    for m in movies:
        print(m["title"])
    # return movies

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
# TODO: Implement GET /movies/top (Task 1 + Task 2)
# BONUS: GET /directors/{director_id}/movies
# BONUS: GET /movies/{movie_id}/reviews
