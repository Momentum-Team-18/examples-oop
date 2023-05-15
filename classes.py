class Hero:
    # blueprint for constructing a hero
    def __init__(self, name, courage):
        self.name = name
        self.courage = courage

    def __str__(self):
        # can override the built in behavior of the 'magic methods' that come with a class in Python
        return f'{self.name} the {self.courage} hero'

    def guess_letter(self):
        # method of the class Hero. Only instances of Hero can do it
        letter = input('Guess a letter: ')
        print(f'{self.name} guessed {letter}')
        return letter


class Dragon:
    def __init__(self, name, scariness):
        self.name = name
        self.scariness = scariness

    def __str__(self):
        return f'{self.name} the {self.scariness} dragon'


luke = Hero('Luke', 'very brave')
# when we make one instance of a class, we 'instantiate' that class
# python is calling the __init__() method
jvn = Hero('Jonathan Van Ness', 'very brave')


dragon1 = Dragon('Doug', 'not very scary')
dragon2 = Dragon('Cleo', 'terrifying')
dragon3 = Dragon('Moss', 'moderately scary')

luke.guess_letter()
