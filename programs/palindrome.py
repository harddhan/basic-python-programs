def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def main():
    text = input("Enter a string: ")
    if is_palindrome(text):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


if __name__ == "__main__":
    main()
