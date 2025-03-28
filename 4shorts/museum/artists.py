"""Module providing functions to work with internet."""
import requests

def get_artists(query, limit):
    """"Provides artists list by query"""
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search", 
            {"q": query, "limit": limit},
            timeout=10
            )
        response.raise_for_status()
    except requests.HTTPError:
        return []

    content = response.json()
    return [artist["title"] for artist in content["data"]]
