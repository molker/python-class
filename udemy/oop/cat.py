# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat0 = Cat('Misty', 12)
cat1 = Cat('Maddy', 12)
cat2 = Cat('Sadie', 15)

# 2 Create a function that finds the oldest cat


def oldestCat(*args):
    oldest = args[0]
    for cat in args:
        if cat.age > oldest.age:
            oldest = cat
    return oldest


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldestCat(cat0,cat1,cat2).age} years old.')
