people = [
    {"name": "Shilla", "house": "Gryffindor"},
    {"name": "Milly", "house": "Kales"},
    {"name": "Stephen", "house": "Dutch"}
]

people.sort(key=lambda person: person["name"])

print(people)
