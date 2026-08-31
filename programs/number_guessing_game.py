import random


def main():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"Correct! You took {attempts} attempts")
            break


if __name__ == "__main__":
    main()
