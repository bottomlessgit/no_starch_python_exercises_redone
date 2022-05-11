places = ["new zealand", "japan", "venezuela", "egypt", "brussels", "morocco"]
print("Places:\n", places)
print("\nPlaces(sorted using sorted()):\n", sorted(places))
print("\nPlaces(unchanged): ", places)
print("\nPlaces(reverse sorted using sorted(reverse = True)):\n",
    sorted(places, reverse = True))
print("\nPlaces(unchanged):\n", places)
places.reverse()
print("\nPlaces(order reversed permanently using reversed()):\n", places)
places.sort()
print("\nPlaces(sorted permanently using sort():\n", places)
places.sort(reverse = True)
print("\nPlaces(sorted permanently using sort():\n", places)

