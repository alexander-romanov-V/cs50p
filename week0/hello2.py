""" functions """
    
def main(): 
    hello()
    name = input("What's your name? ")
    hello(name.title())

def hello(to="world"):
    print("hello,", to)

main()