# Q12: Create a TemperatureConverter class with a static method to convert Celsius to Fahrenheit.
print("Q12: Create a TemperatureConverter class with a static method to convert Celsius to Fahrenheit.")
class Temp_Conv:
    @staticmethod
    def c_to_f(c):
        return (c * 9/5) + 32

print(f"25 C = {Temp_Conv.c_to_f(25)}F")