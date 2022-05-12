#lex_auth_012751861844041728222
#Start writing your code here

class Parrot:
    __counter = 7000

    def __init__(self, name, color):
        Parrot.__counter += 1
        self.__name = name
        self.__color = color
        self.__unique_number = Parrot.__counter

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_unique_number(self):
        return self.__unique_number


parrot1 = Parrot("parrot1", "Green")
parrot2 = Parrot("parrot2", "Red")
print(parrot1.get_name(), parrot1.get_color(), parrot1.get_unique_number())
print(parrot2.get_name(), parrot2.get_color(), parrot2.get_unique_number())
