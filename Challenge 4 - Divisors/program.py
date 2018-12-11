def main():
    print_header()
    calculate_divisors()


def print_header():
    print("------------------------------------------")
    print("                Divisors")
    print("------------------------------------------")
    print()


def calculate_divisors():
    user_input = int(input("Please enter a random integer. "))

    base_list = list(range(1, user_input))

    divisor_list = []

    for i in base_list:
        if user_input % i == 0:
            divisor_list.append(i)

    user_input_string = str(user_input)
    print("The number {} divides evenly by the following numbers.".format(user_input))
    for i in divisor_list:
        print(i)


if __name__ == "__main__":
    main()
