#!/bin/usr/env python3

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def get_celsius(self):
        return self.celsius

    def get_fahrenheit(self):
        return self.celsius * 1.8 + 32

    def get_unit(self):
        return 'C'

# Usage
celsius_temperature = 28.5
temperature_obj = Temperature(celsius_temperature)

print("Temperature in Celsius:", temperature_obj.get_celsius())
print("Temperature in Fahrenheit:", temperature_obj.get_fahrenheit())
print("Temperature unit:", temperature_obj.get_unit())
