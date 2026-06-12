# Q13: Create a Utility class with a static method to check whether a number is even or odd.
print("Q13: Create a Utility class with a static method to check whether a number is even or odd.")
class Utility:
    @staticmethod
    def check_even_odd(num):
        if num % 2 == 0:
            return "Even"
        return "Odd"

print("The given no. is ", Utility.check_even_odd(7))