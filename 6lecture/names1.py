# with open("names.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
    
# for line in lines:
#     print("hello,", line.rstrip())

# Pythinoc way - iterate line within file
with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print("hello,", line.rstrip())