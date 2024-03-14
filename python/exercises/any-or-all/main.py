length = int(input())
numbers = list(map(int, input().split()))

print(all([0 < number for number in numbers]) == any([(0 <= number < 10 or number % 11 == 0) for number in numbers]))
