# OOP
'''
Notes
    self is just like "this." in javascript
    class methods vs static methods
        static methods are associated with the class but dont use cls/self
        both can be used without an instanciated object
    there's no true private variables
        way around it: use _ before variable name 
'''


class PlayerCharacter:
    # Class Object Attributes
    health = 10

    # constructor
    def __init__(self, name, game):
        # Attributes
        self.name = name
        self.game = game

    def run(self):
        print('run')

    def introduction(self):
        print(f'My name is {self.name} and I\'m from {self.game}')

    # decorator
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Added Player', str(num1 + num2))

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Samus', 'Metroid')
player1.suit = 'varia'
player2 = PlayerCharacter('Trevor', 'Castlevania')

print(player1.name)
player2.run()

# location in memory
print(player1)

player2.introduction()
print(PlayerCharacter.adding_things(1, 2))
