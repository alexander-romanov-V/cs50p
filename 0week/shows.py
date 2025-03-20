SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family "
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    
    print(cleaned_shows)                # show as list is actually presented in pytho - ['one', 'two', 'three']

    print(', '.join(cleaned_shows))     # actually use init string (', ') as separator between all elements of argument list

    print('|'.join(cleaned_shows))

main()
