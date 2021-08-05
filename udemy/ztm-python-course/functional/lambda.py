# Exercise
# create a lambda expression that will square our list
my_list = [5, 4, 3]

print(list(map(lambda a: a**2, my_list)))

# sort a list of tuples based on second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])

print(a)
