cities = ["new york", "chicago", "houston", "memphis", "atlanta", "portland", "los angeles"]

print("Original City List:")
print(cities)

print("Length of Original City List:")
print(len(cities))

print("Temporarily sorted City List:")
print(sorted(cities))

print("Temporarily reverse-sorted City List:")
print(sorted(cities, reverse = True))

print("City List Permanently Reversed:")
cities.reverse()
print(cities)

print("City List Permanently Reversed Back:")
cities.reverse()
print(cities)

print("City List Permanently Sorted:")
cities.sort()
print(cities)

print("City List Reverse Sorted:")
cities.sort(reverse = True)
print(cities)

print("City List with " + cities.pop() + " Permanently Removed:")
print(cities)

index = 2
print("City List with " + cities[index] + " Permanently Removed:")
del cities[index]
print(cities)