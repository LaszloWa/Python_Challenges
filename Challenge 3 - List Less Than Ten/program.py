
print("-----------------------------------------------------")
print("              List Less Than Number")
print("-----------------------------------------------------")
print()
print("Hi. This app contains a list.\nAfter entering a number between 0 and 100,\nyou will be shown all values from that list\nthat are less than your selected number.")

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

user_input = int(input("Please pick a number between 0 and 100. "))

new_list = []

for i in my_list:
    if i < user_input:
        new_list.append(i)

print(new_list)
