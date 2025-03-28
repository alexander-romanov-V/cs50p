"""Modules providing functions to work with internet and system."""
import sys
import requests


def main():
    """Main code block."""
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist},
            timeout=10
            )
        response.raise_for_status()         # add raise exception HTTPError if not 200 OK
    except requests.HTTPError:
        sys.exit("Couldn't complete request!")

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")

if __name__ == "__main__":
    main()
