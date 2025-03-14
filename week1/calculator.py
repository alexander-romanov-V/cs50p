""" int """
""" operations: + - * / % """

x = int(input("What's x? "))    # int
y = int(input("What's y? "))

print(x + y)


""" float """
x = float(input("What's x? "))   # float
y = float(input("What's y? "))

z = round(x + y)
print(f"{z:,}")     # add , every 1000 -> 1,000; 1000000 -> 1,000,000

z= x / y
print(f"{z:.2f}")   # round - 2 digits

z = round(x / y, 2)
print(z)
