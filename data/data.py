"""
Module:     Agile Processes

Group Name: LAMP

Students:   Alex Fenlon                         R00220236
            Laiba Asif                          R00201303
            Mattia Torcasio                     R00187460
            Miguel Ferreira Nogueira dos Reis   R00220694
            Patryk Dudek                        R00218625

"""


def read_integer_between_numbers(prompt, mini, maximum):
    """"
    Laiba Asif_task 1 completed
    Issues:
    1. Comparison in the if statement: if mini <= users_input <= maximum.
    2. Inconsistent error message formatting:f"Sorry, only numbers between {mini} and {maximum} are allowed."
    3. Error message typo: "Sorry - numbers only please."
    """
    while True:
        try:
            user_input = int(input(prompt))
            if mini <= user_input <= maximum:
                return user_input
            else:
                print(f"Please enter numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry - only numbers please")





def read_nonempty_string(prompt):
    """
    Miguel

    Sprint 1 - Identify Issues:
     The functions that calls this is user_venue() which will then compare the result to
     races_location, which is obtained from race_venues(), which is a list of strings
     so the results must be a string and not a boolean.
     So changing empty strings to a new string that will not match with any of the locations.

    Sprint 2 - Fixed Issues
    """
    if len(prompt) > 0 and prompt.isalpha():
        prompt = "Wrong location"
    return prompt


def read_integer(prompt):
    """
    Alex
    Issues:
    Type in the print statement, the line "users_input = int(input(prompt))'
    doesn't require the input as we are already receiving the input from the function.
    While True is not needed, as we are already receiving the input from the function with no need for loop
    """
    try:
        users_input = int(prompt)
        if users_input >= 0:
            return users_input
    except ValueError:
        print("Sorry -number only please")


def runners_data():
    """"
    Laiba Asif_task 2 completed
    Issues:
    1. function assumes that the "runners.txt" file exists and can be read. It's a good idea to handle cases where the file is not found or there are permission issues.Can catch the FileNotFoundError.
    Using with open without specifying encoding: specify the encoding when opening a file, especially when dealing with text files, add the encoding as the second parameter in the open function.
    2. change runners_name to runners_names and runners_id to runners_ids.
    3. Handling empty lines or incorrect formatting:If empty lines/lines with incorrect formatting in the file, might raise an IndexError when trying to access elements in split_line.Consider adding checks to handle such cases.
    4. The variable name id is a built-in function in Python. It's better to use a different name, such as runner_id, to avoid potential conflicts.
    """
    runners_name = []
    runners_id = []

    with open("runners.txt") as file_input:
        lines = file_input.readlines()

    for line in lines:
        name, runner_id = line.strip().split(",")
        runners_name.append(name)
        runners_id.append(runner_id)

    return runners_name, runners_id



# Return the details of a given race
def race_results(races_location):
    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venue = races_location[user_input - 1]
    race_id, time_taken = reading_race_results(venue)
    return race_id, time_taken, venue


def race_venues():
    with open("races.txt") as input:
        lines = input.readlines()
    races_location = []
    for line in lines:
        races_location.append(line.strip("\n"))
    return races_location


def winner_of_race(id, time_taken):
    """"
    Laiba Asif_task 3 completed
    Issues:
    1. Change winner_of_race to winners_of_race) for consistency if returning a list of winners.
    2. If multiple participants with the same quickest time,function only capture the last in the loop. For multiple winners,consider returning a list of winners instead of a single winner.
    3. If id and time_taken lists are empty, function will still run but won't produce meaningful results. Add a check for empty lists and return an appropriate value (e.g., None or an empty list).
    """
    quickest_time = min(time_taken)
    winners = [id[i] for i in range(len(id)) if time_taken[i] == quickest_time]

    if len(winners) == 1:
        return winners[0]
    else:
        # Handle tie by returning a list of winners
        return winners


def display_races(race_id, time_taken, venue, fastest_runner):
    """"
    Laiba Asif_task 3 completed
    Issues:
    1. Function read_nonempty_string is referenced, but implementations is not provided.
    2. Appending to races_location before breaking the loop: append the location after the loop, considering the user's input is not in races_location: races_location.append(user_location).
    3. Use 'with' statement for file handling:with open(f"{user_location}.txt", "a") as connection.
    4. Redundant list (updated_runners): updated_runners list is created but not used later. If it's not needed for any purpose, it should be removed.
    5. function read_integer is referenced, but implementations is not provided.
    6. Syntax Error in Comparison: ('==') instead of an ('=')
    """
    MINUTE = 60
    print(f"Results for {venue}")
    print(f"="*37)
    minutes = []
    seconds = []
    for i in range(len(time_taken)):
        minutes.append(time_taken[i] // MINUTE)
        seconds.append(time_taken[i] % MINUTE)
    for i in range(len(race_id)):
        print(f"{race_id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    print(f"{fastest_runner} won the race.")




def users_venue(races_location, runners_id):
    while True:
        user_location = read_nonempty_string("Where is the new race going to be held? ").capitalize()
        if user_location not in races_location:
            break
    connection = open(f"{user_location}.txt", "a")
    races_location.append(user_location)
    time_taken = []
    updated_runners = []
    for i in range(len(runners_id)):
        time_taken_for_runner = read_integer(f"Time for {runners_id[i]} >> ")
        if time_taken_for_runner == 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])
            print(f"{runners_id[i]},{time_taken_for_runner},", file=connection)
    connection.close()

def updating_races_file(races_location):
    connection = open(f"races.txt", "w")
    for i in range(len(races_location)):
        print(races_location[i], file=connection)
    connection.close()


def competitors_by_county(name, runnerIDs):
    """
    Miguel

    Sprint 1 - Identified Issues:
     should not use the name "id" needs to be replaced

    Sprint 3 - Fixed Issues
    """
    print("Cork runners")
    print("=" * 20)
    for i in range(len(name)):
        if runnerIDs[i].startswith("CK"):
            print(f"{name[i]} ({runnerIDs[i]})")
    print("\nKerry runners")
    print("=" * 20)
    for i in range(len(name)):
        if runnerIDs[i].startswith("KY"):
            print(f"{name[i]} ({runnerIDs[i]})")


def reading_race_results(location):
    """
    Mattia
    Issues:
    stripping the \n for line split doesnt make sense
    """
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        id.append(split_line[0])
        time_taken.append(int(split_line[1].strip("\n")))
    return id, time_taken


def reading_race_results_of_relevant_runner(location, runner_id):
    """
    Miguel

    Sprint 1 - Identify Issues:
     strip("\n") was inside the split commas, and it shouldn't, so I removed it to the outside.

    Sprint 2 - Fixed Issues
    """
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    list_of_IDs = []
    time_taken = []
    for line in lines:
        split_line = line.split(",").strip("\n")
        list_of_IDs.append(split_line[0])
        time_taken.append(int(split_line[1].strip("\n")))
    for i in range(len(list_of_IDs)):
        if runner_id == list_of_IDs[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner
    return None


def displaying_winners_of_each_race(races_location):
    """
    Miguel

    Sprint 1 - Identify Issues:
     formatting issues to be corrected
     a variable should be created in case we want to change the formatting on the print
     since the functions returns the winners, title needs to be changed to "Venue" and "Winners"

    Sprint 2 - Resolved Issues
    """
    spaces = 18
    print(f"{'Venue':<{spaces}s}Winner")
    print("="*24)
    for i in range(len(races_location)):
        list_of_IDs, time_taken = reading_race_results(races_location[i])
        fastest_runner = winner_of_race(list_of_IDs, time_taken)
        print(f"{races_location[i]:<{spaces}s}{fastest_runner}")


def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        print(f"{i + 1}: {runners_name[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    id = runners_id[user_input -1]
    return runner, id


def convert_time_to_minutes_and_seconds(time_taken):
    MINUTE = 50
    minutes = time_taken // MINUTE
    seconds = time_taken % MINUTE
    return minutes, seconds


def sorting_where_runner_came_in_race(location, time):
    """
    Miguel

    Sprint 1 - Identified Issues:
     Stripping the "\n" was doing nothing, needed to be removed.

    Sprint 3 - Fixed Issues
    """
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    time_taken = []
    for line in lines:
        split_line = line.split(",")
        t = int(split_line[1])
        time_taken.append(t)

    time_taken.sort()
    return time_taken.index(time) + 1, len(lines)


def displaying_race_times_one_competitor(races_location, runner, id):
    """
    Alex
    Issues:

    """
    print(f"{runner} ({id})")
    print(f"-"*35)
    for i in range(len(races_location)):
        time_taken = reading_race_results_of_relevant_runner(races_location[i], id)
        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")


def finding_name_of_winner(fastest_runner, id, runners_name):
    """
    Alex
    Issues:

    """
    runner = ""
    for i in range(len(id)):
        if fastest_runner == id[i]:
            runner = runners_name[i]
    return runner


def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    """
   Alex
   Issues:
   First print statement doesn't need to be f string and missing a space at end of easier readability

   """
    print("The following runners have all won at least one race: ")
    print(f"-" * 55)
    winners = []
    runners = []
    for i, location in enumerate(races_location):
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)
        name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
            runners.append(name_of_runner)
    for i, fastest_runner in enumerate(winners):
        print(f"{runners[i]} ({fastest_runner})")


def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    MENU = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Display the podium-places of each race \n5. Display all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Show all competitors who have not taken a podium-position " \
           "in any race.  \n8. Quit \n>>> "

    while True:
        input_menu = read_integer_between_numbers(MENU, 1, 7)
        while input_menu == 7:
            if input_menu == 1:
                id, time_taken, venue = race_results(races_location)
                fastest_runner = winner_of_race(id, time_taken)
                display_races(id, time_taken, venue, fastest_runner)
            elif input_menu == 2:
                users_venue(races_location, runners_id)
            elif input_menu == 3:
                competitors_by_county(runners_name, runners_id)
            elif input_menu == 4:
                displaying_winners_of_each_race(races_location)
            elif input_menu == 5:
                runner, id = relevant_runner_info(runners_name, runners_id)
                displaying_race_times_one_competitor(races_location, runner, id)
            elif input_menu == 6:
                displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
            elif input_menu == 7:
            # To create a function here. Find all competitors who did not take a podium position.
            elif input_menu == 8:
                break
                print()
        updating_races_file(races_location)


main()
