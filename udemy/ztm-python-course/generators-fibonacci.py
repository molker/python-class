# Exercise: Fibonacci Numbers
# print version
def fib(number):
    last_pos = 0
    position = 1
    for i in range(number):
        yield last_pos
        temp = position
        position = position + last_pos
        last_pos = temp


for x in fib(20):
    print(x)


# list version
def fib2(number):
    last_pos = 0
    position = 1
    result = []
    for i in range(number):
        result.append(last_pos)
        temp = position
        position = position + last_pos
        last_pos = temp
    return result


print(fib2(20))
