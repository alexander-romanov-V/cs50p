distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    while True:
        spacecraft = input("Enter a spacecraft: ")
        try:
            au = float(distances[spacecraft])
        except KeyError:
            pass
        except ValueError:
            print(f"Can't convert '{distances[spacecraft]}' to a float")
            return
        else:
            m = convert(au)
            print(f"{m} m away")
            break

# def main():
#     while True:
#         spacecraft = input("Enter a spacecraft: ")
#         try:
#             au = distances[spacecraft]
#         except KeyError:
#             pass
#         else:
#             try:
#                 au = float(au)
#             except ValueError:
#                 au = float(au.removesuffix("AU"))
#             m = convert(au)
#             print(f"{m} m away")
#             break

def convert(au):
    return au * 149597870700

main()