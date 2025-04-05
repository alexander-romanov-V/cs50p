def main():
    expresssion = input("Expression: ")
    x, y, z = expresssion.split(" ")
    x = float(x)
    z = float(z)
    res = 0
    match y:
        case "+":
            res = x + z
        case "-":
            res = x - z
        case "*":
            res = x * z
        case "/":
            if z == 0:
                print("Can't divide on 0")
                return
            res = x / z
        case _:
            print("Wrong math symbol")

    print(f"{res:.1f}")


main()
