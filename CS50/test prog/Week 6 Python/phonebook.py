names = ["Yuliia", "David", "John"]

name = input("Name: ")

for n in names:
    if name == n:
        print("Found")
        break
else:
    print("Not Found")

#if name in names:
#   print("Found")
#else:
#   print("Not Found")
#
