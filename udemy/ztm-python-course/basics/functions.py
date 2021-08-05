# Exercise Functions
# write a function called highest_even and find the highest even number
def highest_even(li):
    li.sort(reverse=True)
    for num in li:
        if num % 2 == 0:
            return num
    print('No even numbers found')


print(highest_even([10, 2, 3, 4, 8, 11]))
