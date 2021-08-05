# Example of dunder methods

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

    # you can modify dunder methods if you need it to behave in a certain way
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted!')

    def __call__(self):
        return 'called'


action_figure = Toy('blue', 2)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
del action_figure
print(action_figure())
