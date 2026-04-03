s = input("S: ")#.lower() 
t = s.lower()

if s == "Y" or s == "y":
    print("Agreed")
elif s == "N" or s == "n":
    print("Not agreed")


if t in ["yes", "y"]:
    print("Agreed")
elif t in ["no", "n"]:
    print("Not agreed")
