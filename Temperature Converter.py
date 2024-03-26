def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    choice = input("Choose conversion (C to F / F to C): ").upper()
    if choice == "C TO F":
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
    elif choice == "F TO C":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
