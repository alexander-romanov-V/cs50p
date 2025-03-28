"""Package providing a modules with functions to work with museum of art."""
from museum.artwork import get_artwork
from museum.artists import get_artists
# 'museum' is a PACKAGE (folder with some modules and special empty file __init__.py)

# from artwork import get_artwork
# import artists

def main():
    """Main code block."""
    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=3)
    for artist in artists:
        print(f"* {artist}")

    # artwork = input("Artwork: ")
    # artworks = get_artwork(query=artwork, limit=3)
    # for artwork in artworks:
    #     print(f"* {artwork}")


if __name__ == "__main__":
    main()
