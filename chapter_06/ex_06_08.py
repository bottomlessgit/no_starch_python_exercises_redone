pet1 = {
    "pet name" : "jane air",
    "pet species" : "finch",
    "owner name" : "charlotte bronte",
}

pet2 = {
    "pet name" : "damned spot",
    "pet species" : "dog",
    "owner name" : "willy shakespeare",
}

pet3 = {
    "pet name" : "the bluest bird",
    "pet species" : "bluebird",
    "owner name" : "Toni Morrison",
}

pet4 = {
    "pet name" : "brief candle",
    "pet species" : "dog",
    "owner name" : "willy shakespeare",
}

pet5 = {
    "pet name" : "camila",
    "pet species" : "chameleon",
    "owner name" : "paul simon",
}

pets = [pet1, pet2, pet3, pet4, pet5]

print("The colorful pets we have in our care are:\n")
for pet in pets:
    for quality, detail in pet.items():
        print(quality.title(), ":", detail.title())
    print()