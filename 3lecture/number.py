try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer!")
else:
    print(f"x is {x}")

# try:
#     print(f"x is {x}")
# except NameError:
#     print("x is not defined!")
