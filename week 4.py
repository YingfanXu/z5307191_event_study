# Exercise 1
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]


def even(test):
    evenum = []
    for number in test:
        if number % 2 == 0:
            evenum.append(number)
    return evenum


res = even(l)
print(res)

list = [2, 3, 10, 14, 20, 21, 25, 13, 15]
new = [x ** 2 for x in list if x ** 2 > 150]

print(f'the new list with value of square greater than 150 is {new}')

# Exercise 2.1
list = [2, 3, 10, 14, 20, 21, 25, 13, 15]
new = [x ** 2 for x in list if x ** 2 > 150]

print(new)

print(f'the new list with value of square greater than 150 is {new}')

# Exercise 2.2

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]

# Approach 1:
# Use a set comprehension to get the unique even values
result1 = list({i for i in numbers if i % 2 == 0})
# Sort the resulting list
result1.sort()
print(result1)

# Approach 2:
# Use a list comprehension that loops over a set of the original list to filter even numbers
result2 = [i for i in set(numbers) if i % 2 == 0]
# Sort the resulting list
result2.sort()
print(result2)
