def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def main():
    p = float(input("Enter principal: "))
    r = float(input("Enter rate: "))
    t = float(input("Enter time: "))
    print(simple_interest(p, r, t))


if __name__ == "__main__":
    main()
