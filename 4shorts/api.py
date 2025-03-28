import requests, sys

def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")
    
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist}
            )
        response.raise_for_status()         # additional raise exception HTTPError if response is not = 200 OK
    except requests.HTTPError:
        sys.exit("Couldn't complete request!")

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")

if __name__ == "__main__":
    main()