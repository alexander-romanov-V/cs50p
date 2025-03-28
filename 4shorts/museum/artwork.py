"""Module providing functions to work with internet."""
import requests

def get_artwork(query, limit):
    """"Provides artworks list by query"""
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", 
            {"q": query, "limit": limit},
            timeout=10
            )
        response.raise_for_status()
    except requests.HTTPError:
        return []

    content = response.json()
    return [artwork["title"] for artwork in content["data"]]
