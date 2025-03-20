""" 
Multiline 
comment
"""

# Ask user for their name
# name = input("What's your name? ")

# name = name.strip()         # remove lead and trailing spaces
# name = name.capitalize()    # make 1st letter capital, and other - not
# name.strip().capitalize() # make all that at one time

# name = name.title()         # capitalize each word in sentence
name = input("What's your name? ").strip().title()    # apply all transforms on return value of input()

# Say hello to user
# print('hello, ', end='')
# print(name)
# print("hello,", name)       # auto add space [sep=' '] between arguments
# print("hello, " + name)     # concatenate/join strings
print(f"hello, {name}")     # Format string (f-string) with variable inside


# Split user's name into first and last name
first, last = name.split(' ')   # error, if more than 2 words (whitespaces)
print(f"hello, {first}")












