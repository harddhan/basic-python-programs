def calculate_bmi(weight, height):
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {bmi_category(bmi)}")


if __name__ == "__main__":
    main()
