people = {
    "Yuliia": "+1-617-495-1000",
    "David": "+1-617-495-1000",
    "John": "+1-949-468-2750",
}

name = input("Name: ")

if name in people:
    print(f"Found {name} : {people[name]}")
else:
    print(f"{name} not found")
