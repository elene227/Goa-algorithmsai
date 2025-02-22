binary = [29, 1, 14, 25, 15, 21, 18, 5, 1, 4, 20, 8, 9, 19, 53, 35, 6, 25, 15, 21, 3, 1, 14, 18, 5, 1, 4, 20, 8, 9, 19, 55, 20, 8, 1, 20, 13, 5, 1, 14, 19, 25, 15, 21, 1, 12, 18, 5, 1, 4, 25]

user_input = input("Please type 'yes' to print translation: ")

if user_input.lower() == "yes":
    print(binary)
elif user_input.lower() == "no":
    print("Error: You typed no.")
else:
    print("Invalid input, please type 'yes' or 'no'.")
