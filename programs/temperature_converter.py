def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter choice (1/2): ")
    value = float(input("Enter temperature: "))

    if choice == "1":
        print(celsius_to_fahrenheit(value))
    elif choice == "2":
        print(fahrenheit_to_celsius(value))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
