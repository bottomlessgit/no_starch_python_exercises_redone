rivers = {
    "nile" : "egypt",
    "mississippi" : "united states of america",
    "amazon" : "brazil",
    "parana" : "brazil",
    "yangtze" : "china",
}

for river, country in rivers.items():
    print("The", river.title(), "runs through", country.title())

print("\nThe rivers on our list are:")
for river in rivers.keys():
    print("\t" + river.title())

print("\nThe countries on our list are:")
for country in set(rivers.values()):
    print("\t" + country.title())

