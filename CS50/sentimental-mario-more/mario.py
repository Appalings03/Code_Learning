from cs50 import get_int
# prompt user for input
while True:
    h = get_int("Height: ")
    # break when input > than 0
    if h >= 1 and h < 9:
        break

# loop for the height
for i in range(h):
    # loop for the space before '#'
    for _ in range(1, h - i):
        print(" ", end="")
    # loop for the '#'
    for _ in range(i + 1):
        print("#", end="")
    # print for the '\n'
    print("  ", end="")
    # loop for the '#'
    for _ in range(i + 1):
        print("#", end="")
    # new line
    print()
