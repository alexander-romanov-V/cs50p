import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for name in sys.argv[1:-1]:                       # slice list (start from 1, and except last one -1)
    print("hello, my name is", name)
