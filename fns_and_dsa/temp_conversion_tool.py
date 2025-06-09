FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_temperature_input():
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            print(f"{temp}°C is {convert_to_fahrenheit(temp):.2f}°F")
        elif unit == "F":
            print(f"{temp}°F is {convert_to_celsius(temp):.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    get_temperature_input()