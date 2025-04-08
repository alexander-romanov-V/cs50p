"""e-mail validation with RegExp"""

import re
# RegExp symbols:
# .       any character except a newline
# *       0 or more repetitions
# +       1 or more repetitions
# ?       0 or 1 repetition
# {m}     m repetitions
# {m,n}   m-n repetitions
# ^       matches the start of the string
# $       matches the end of the string or just before the newline at the end of the string
# []      set of characters (match any of this characters))
# [^]     complementing the set (NOT match any of this characters)
# [a-z]   range of characters (from a till z)
# (ab|cd) any group of characters (ab or cd)
# \d      decimal digit               == [0-9]
# \D      not decimal digit           == [^0-9]
# \s      whitespace characters       == [ \t]
# \S      not whitespace characters   == [^ \t]
# \w      word character .. as well as numbers and the underscore == [a-zA-Z0-9_]
# \W      not word character          == [^a-zA-Z0-9_]

# flags:
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL       - interpret . as 'any characters PLUS NEWLINE'


email = input("What's your email? ").strip()

# RAW string - r"text"
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
# if re.search(r"^\w+@\w+\.edu$", email):
if re.search(r"^\w+@\w+\.edu$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
