import sys

def main():
    # latitude = 42.376
    # longitude = -71.115

    coordinates = (42.376, -71.115)
    print (f"Latitude: {coordinates[0]}")
    print (f"Longitude: {coordinates[1]}")

    latitude, longitude = coordinates
    print (f"Latitude: {latitude}")
    print (f"Longitude: {longitude}")

    # coordinates[0] = -42.376        # ERROR, tupple do not support assigning
    coordinate_list = [42.376, -71.115]

    print(f"Tupple is {sys.getsizeof(coordinates)} bytes")
    print(f"List is {sys.getsizeof(coordinate_list)} bytes")

main()