""""task 1 completed"""

def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            user_input = int(input(prompt))
            if mini <= user_input <= maximum:
                return user_input
            else:
                print(f"Please enter numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry - only numbers please")

# Example usage:
# result = read_integer_between_numbers("Enter a number: ", 1, 100)
# print("You entered:", result)