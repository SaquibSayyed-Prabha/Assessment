# Q20: Create an Employee class with private data and update it using setter methods.
print("Q20: Create an Employee class with private data and update it using setter methods.")
class Employee:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

e = Employee()
e.set_name("Saquib")
print(e.get_name())