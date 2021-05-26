class User():
    def __init__(self, username):
        self.username = username

    def sign_in(self):
        print(f'{self.username} logged in')


class Wizard(User):
    def __init__(self, username, name, weapon):
        super().__init__(username)
        self.name = name
        self.weapon = weapon

    def attack(self):
        print(f'{self.name} cast fireball')


class Archer(User):
    def __init__(self, username, name, weapon):
        super().__init__(username)
        self.name = name
        self.weapon = weapon

    def attack(self):
        print(f'{self.name} fired using {self.weapon}')


class Classless(Wizard, Archer):
    pass

# Attack can be called on either and get their specific method
# good example of polymorphism


wizard = Wizard('somegiraffe', 'Kevin', 'Arcane Focus')
archer = Archer('ZeroToHero', 'Andrei', 'Hand Crossbow')
print(wizard.sign_in())
print(wizard.attack())
print(archer.sign_in())
print(archer.attack())

# Wizard comes first in the inheritance, so if they had different parameters
# the wizards would be put before the archer
someguy = Classless('justsomeguy', 'Dan', 'stick')