def main():
    print_header()
    number = int(input("Please pick a random integer (whole number). "))
    odd_or_even(number)
    two_numbers_divided()


def print_header():
    print("-----------------------------------------")
    print("             Odd or Even?")
    print("-----------------------------------------")
    print()


def odd_or_even(number):
    if number % 4 == 0:
        print("{} is a multiple of 4.".format(number))
    elif number % 2 == 0:
        print("{} is an even number.".format(number))
    elif number % 2 != 0:
        print("{} is an odd number.".format(number))
    else:
        print("Sorry, there seems to have been an error.")


def two_numbers_divided():
    print("Please enter two whole numbers.")
    num = int(input("Number 1: "))
    check = int(input("Number 2: "))

    if num % check == 0:
        print("{} divides evenly by {}.".format(num, check))
    else:
        print("{} does not divide evenly by {}.".format(num, check))


if __name__ == "__main__":
    main()
