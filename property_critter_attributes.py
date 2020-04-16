# Property Critter
# Demonstrates properties

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, color):
        print("A new critter has been born!")
        self.__name = name
        self.__color = color

    color = ["red", "green", "blue", "purple", "orange", "white"]

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

    def talk(self):
        print("\nHi, I'm", self.name)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        if new_color not in self.colors:
            print("That's not a critter color.")
        else:
            self.__color = new_color
            self.nameOut()

    def nameOut(self):
        print("Mycritter's name is now***", self.color, self.name, "***")

            
# main
crit = Critter("Poochie")
crit.talk()

print("\nMy critter's name is:", end= " ")
print(crit.name)

print("\nAttempting to change my critter's name to Randolph...")
crit.name = "Randolph"
print("My critter's name is:", end= " ")
print(crit.name)

print("\nAttempting to change my critter's name to the empty string...")
crit.name = ""
print("My critter's name is:", end= " ")
print(crit.name)

input("\n\nPress the enter key to exit.")
