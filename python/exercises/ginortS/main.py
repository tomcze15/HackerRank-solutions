string = input()

small = []
big = []
numbers_odd = []
numbers_even = []

for char in string:
    if char.islower():
        small.append(char)
        continue

    if char.isupper():
        big.append(char)
        continue

    if not char.isdigit():
        continue

    if int(char) % 2 == 0:
        numbers_even.append(char)
        continue

    numbers_odd.append(char)


print(''.join(sorted(small) + sorted(big) + sorted(numbers_odd) + sorted(numbers_even)))
