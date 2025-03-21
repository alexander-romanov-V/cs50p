def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
    print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

def print_square(size):
    print(("#" * size + "\n") * size, end="")

main()