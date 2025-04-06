def main():
    """Main code"""
    grocery_list = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            break
        if item.isprintable():
            grocery_list[item] = grocery_list.get(item, 0) + 1
        # if item in grocery_list:
        #     grocery_list[item] += 1
        # else:
        #     grocery_list[item] = 1

    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item}")


if __name__ == "__main__":
    main()
