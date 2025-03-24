def main():
    camel_var = input("camelCase: ")
    snake_var = ""

    for s in camel_var:
        if s.isupper():
            snake_var += "_" + s.lower()
        else:
            snake_var += s

    print(f"snake_case: {snake_var}")




main()