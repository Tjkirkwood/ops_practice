#!/usr/bin/env python3

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
    except ValueError:
        print("Invalid input. Please enter a valid temperature in Celsius.")

if __name__ == "__main__":
    main()

