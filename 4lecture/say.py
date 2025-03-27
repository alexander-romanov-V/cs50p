# pip install cowsay
import cowsay, sys

if len(sys.argv) == 2:
    # cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1]) # type: ignore