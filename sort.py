numbers = [55, 12, 18, -14, 56, 33, 122, 1, 80, -33]

while len(numbers) > 0:
    smallest = min(numbers)
    print(smallest)
    numbers.remove(smallest)
    print(numbers)
