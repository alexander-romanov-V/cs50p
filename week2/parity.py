# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x= int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    # Option 3:
    return True if n % 2 == 0 else False 
    # 
    # Option 2:
    # return n % 2 == 0
    # 
    # Option 1:
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

main()