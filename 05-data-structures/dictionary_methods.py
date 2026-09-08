intro = {
    "name": "Afaq",
    "class": 12,
    "subjects": ["math", "chemistry", "biology"]
}

# it access a single value by key
print(intro["name"])

# this print the whole dictionary
print(intro)

# this print only the keys
print(intro.keys())

#it only print the values
print(intro.values())

# it print the keys and values pair by pair
print(intro.items())

# it safely returns None if the key doesn't exist, instead of crashing
print(intro.get("cgpa"))

# it adds a new key and value pair (or updates an existing one)
intro.update({"city": "mardan"})
print(intro)