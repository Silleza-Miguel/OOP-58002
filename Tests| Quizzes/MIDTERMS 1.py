class TemperatureConversion:
    def __init__(self, temp):
        self._temp = temp


class CelsiusToFahrenheit(TemperatureConversion):
    def conversion(self):
        print(str((self._temp * 9/5) + 32) + " Fahrenheit")


class FahrenheitToCelsius(TemperatureConversion):
    def conversion(self):
        print(str((self._temp - 32) * 5/9) + " Celsius")


class CelsiusToKelvin(TemperatureConversion):
    def conversion(self):
        print(str(self._temp + 273.15) + " Kelvin")


class KelvinToCelsius(TemperatureConversion):
    def conversion(self):
        print(str(self._temp - 273.15) + " Celsius")

class KelvinToFahrenheit(TemperatureConversion):
    def conversion(self):
        print(str((self._temp - 273.15) * 9/5 + 32) + " Fahrenheit")


class FahrenheitToKelvin(TemperatureConversion):
    def conversion(self):
        print(str((self._temp - 32) * 9/5 + 237.15) + " Kelvin")


type = ["Celsius", "Fahrenheit", "Kelvin"]

print("*pls use the approriate inputs only so my program doesnt go down the trash*\n")
print("Options:\n"
      f"1. {type[0]}\n"
      f"2. {type[1]}\n"
      f"3. {type[2]}\n")

choice = int(input("Which temperature would you like to convert (1-3)? "))

if choice == 1:
    temp = float(input(f"Enter the temperature in {type[0]}: "))
    C2K = CelsiusToKelvin(temp).conversion()
    C2F = CelsiusToFahrenheit(temp).conversion()

elif choice == 2:
    temp = float(input(f"Enter the temperature in {type[1]}: "))
    F2C = FahrenheitToCelsius(temp).conversion()
    F2K = FahrenheitToKelvin(temp).conversion()

elif choice == 3:
    temp = float(input(f"Enter the temperature in {type[2]}: "))
    K2C = KelvinToCelsius(temp).conversion()
    K2F = KelvinToFahrenheit(temp).conversion()