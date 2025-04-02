# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names):
#     print(f"hello, {name}")

# Pythonic way - SORT file IN PLACE
with open("names.txt", encoding="utf-8") as file:
    for line in sorted(file, reverse=True):
        print("hello,", line.rstrip())
