""" tASK1 """

def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            # 01 Comparison in the if statement: if mini <= users_input <= maximum:
            if maximum <= users_input >= mini:
                return users_input
            else:
                # 02 Inconsistent error message formatting:f"Sorry, only numbers between {mini} and {maximum} are allowed."
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            # 03 Error message typo: "Sorry - numbers only please."
            print("Sorry -numbor olny please")

""" tASK2 """

def runners_data():
    # 01 function assumes that the "runners.txt" file exists and can be read. It's a good idea to handle cases where the file is not found or there are permission issues.Can catch the FileNotFoundError.
    # Using with open without specifying encoding: specify the encoding when opening a file, especially when dealing with text files, add the encoding as the second parameter in the open function.
    with open("runners.txt") as input:
        lines = input.readlines()
   # 02 change runners_name to runners_names and runners_id to runners_ids.
    runners_name = []
    runners_id = []
    for line in lines:
     # 03 Handling empty lines or incorrect formatting:If empty lines/lines with incorrect formatting in the file, might raise an IndexError when trying to access elements in split_line.Consider adding checks to handle such cases.

        split_line = line.split(",")
        runners_name.append(split_line[0])
        # 04 The variable name id is a built-in function in Python. It's better to use a different name, such as runner_id, to avoid potential conflicts.
        id = split_line[1].strip("\n")
        runners_id.append(id)
    return runners_name, runners_id

""" tASK3 """

# 01 change winner_of_race to winners_of_race) for consistency if returning a list of winners.
def winner_of_race(id, time_taken):
# 02 If multiple participants with the same quickest time,function only capture the last in the loop. For multiple winners,consider returning a list of winners instead of a single winner.
    quickest_time = min(time_taken)
# 03 if id and time_taken lists are empty, function will still run but won't produce meaningful results. Add a check for empty lists and return an appropriate value (e.g., None or an empty list).
    winner = ""
    for i in range(len(id)):
        if quickest_time == time_taken[i]:
            winner = id[i]
    return winner


""" tASK4 """


def users_venue(races_location, runners_id):
    while True:
      # 01 function read_nonempty_string is referenced, but implementations is not provided.
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
     # 02 Appending to races_location before breaking the loop: append the location after the loop, considering the user's input is not in races_location: races_location.append(user_location)
        if user_location not in races_location:
            break
   #  03 Use 'with' statement for file handling:with open(f"{user_location}.txt", "a") as connection:
    connection = open(f"{user_location}.txt", "a")
    races_location.append(user_location)
    time_taken = []
  # 04 Redundant list (updated_runners): updated_runners list is created but not used later. If it's not needed for any purpose, it shoud be removed.
    updated_runners = []
    for i in range(len(runners_id)):
       # 05 function read_integer is referenced, but implementations is not provided.
        time_taken_for_runner = read_integer(f"Time for {runners_id[i]} >> ")
        # 06 Syntax Error in Comparison: ('==') instead of an ('='):
        if time_taken_for_runner = 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])
            print(f"{runners_id[i]},{time_taken_for_runner},", file=connection)
    connection.close()