cubes = [num ** 3 for num in range(1,11)]
print(cubes)
print("The first three items on the list are:", cubes[:3])
middle = len(cubes) // 2
print("The middle three items on the list are:", cubes[middle - 1 : middle + 2])
print("The last three items on the list are:", cubes[-3:])