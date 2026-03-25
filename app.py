from flask import Flask, render_template, request
import requests
import math
from functools import lru_cache

app = Flask(__name__)

API_URL = "https://potterapi-fedeperin.vercel.app/en/characters"


@lru_cache(maxsize=1)
def get_all_characters():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def get_pagination_range(current_page, total_pages, window=2):
    start = max(1, current_page - window)
    end = min(total_pages, current_page + window)
    return range(start, end + 1)


@app.route("/")
def home():
    search_query = request.args.get("search", "").strip()
    selected_house = request.args.get("house", "").strip()
    sort_order = request.args.get("sort", "az").strip()
    page = request.args.get("page", 1, type=int)

    error_message = None

    try:
        characters = get_all_characters()
    except requests.exceptions.RequestException:
        characters = []
        error_message = "Could not load data from the Harry Potter API at the moment."

    filtered_characters = [
        character for character in characters
        if search_query.lower() in character.get("fullName", "").lower()
        and (
            selected_house == ""
            or character.get("hogwartsHouse", "").lower() == selected_house.lower()
        )
    ]

    if sort_order == "za":
        filtered_characters = sorted(
            filtered_characters,
            key=lambda c: c.get("fullName", "").lower(),
            reverse=True
        )
    else:
        filtered_characters = sorted(
            filtered_characters,
            key=lambda c: c.get("fullName", "").lower()
        )

    per_page = 12
    total_characters = len(filtered_characters)
    total_pages = math.ceil(total_characters / per_page) if total_characters > 0 else 1

    if page < 1:
        page = 1
    elif page > total_pages:
        page = total_pages

    start = (page - 1) * per_page
    end = start + per_page
    paginated_characters = filtered_characters[start:end]

    pagination_range = get_pagination_range(page, total_pages)

    return render_template(
        "index.html",
        characters=paginated_characters,
        search_query=search_query,
        selected_house=selected_house,
        sort_order=sort_order,
        page=page,
        total_pages=total_pages,
        total_characters=total_characters,
        pagination_range=pagination_range,
        error_message=error_message
    )

app = app