import datetime


def main():
    print_header()
    name = input("What is your name? ")
    birthday = user_age()
    amount_print = int(input("How often would you like to print the message? "))
    user_turn_hundred(name, birthday, amount_print)


def print_header():
    print("----------------------------------")
    print("  Exercise 1 - Character Input")
    print("----------------------------------")
    print()


def user_age():
    birth_year = int(input("What year were you born [YYYY]? "))
    birth_month = int(input("What month were you born [MM]? "))
    birth_day = int(input("What day were you born [DD]? "))

    birthday = datetime.date(year=birth_year, month=birth_month, day=birth_day)
    return birthday


def user_turn_hundred(name, bday, print_amount):
    year_of_hundred = bday.year + 100

    print("{}, you will turn 100 on {}.{}.{}. \n".format(name, bday.day, bday.month, year_of_hundred) * print_amount)


if __name__ == "__main__":
    main()
