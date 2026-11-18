
numbers = [5, 2, 9, 1, 5, 6, 3, 8]


for i in range(len(numbers)):
    byla_zmiana = False
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            byla_zmiana = True
    if not byla_zmiana:
        break

print(numbers)
