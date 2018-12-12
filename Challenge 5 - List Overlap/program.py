import random

print("--------------------------------------------")
print("              List Overlap")
print("--------------------------------------------")
print("This program generates two random lists and\nonly prints the unique values (i.e. only values\nthat are contained in one, but not both lists.")
print()


list_one = []
list_two = []
final_list = []

for i in range(1, random.randint(1, 20)):
    list_one.append(random.randint(1, 10))

for i in range(1, random.randint(1, 20)):
    list_two.append(random.randint(1, 10))

if list_one >= list_two:
    for i in list_one:
        if i in list_two:
            pass
        elif i not in list_two:
            final_list.append(i)
else:
    for i in list_two:
        if i in list_one:
            pass
        elif i not in list_one:
            final_list.append(i)

print(final_list)
