#!/usr/local/bin/python3

import argparse
import json
from collections import OrderedDict


class todo_dict(object):

    # Creates a dictionary with a todo item and priority. Items can be added,
    # removed, or sorted

    def __init__(self, input_dict):
        self.dict = input_dict

    def add_item(self, name, priority):
        self.dict[name] = {"Priority": priority}
        return self.dict

    def get_dict(self):
        return self.dict

    def sort_priority(self):
        self.dict = OrderedDict(sorted(self.dict.items(), key=lambda x: x[1]['Priority']))
        return self.dict

    def del_item(self, key, input_list):
        try:
            # tests if number was given instead of word to access delete func
            # Keeping a list in sync with dictionary allows for the dictionary # to easily be accessed via an index.
            choice = int(key) - 1
            del self.dict[input_list[choice][0]] #deletes dict item from list index
            del input_list[choice]
        except:
            try:
                del self.dict[key]
            except:
                input("\n There is nothing with that name in your todo list. Press any key to continue. \n\n")
        return self.dict

    def convert_to_list(self):
        new_list = [[key, item['Priority']]for key, item in self.dict.items()]
        return new_list

    def reset_dict(self):
        continue_var = input("This will delete all your entries. Are you sure you want to continue? Press <Y> to continue and any other key to abort. \n\n")

        if continue_var.lower() == "y":
            write_JSON(working_dict.reset_dict())
            self.dict = {}
        else:
            input("\n Nothing  was deleted. Press any key to continue. \n")
        return self.dict


def write_JSON(some_JSON_data):
    with open('/usr/local/bin/todo_index.json', 'w') as outfile:
        json.dump(some_JSON_data, outfile, indent=4)


def prepare_input(string_input):
    # Takes a string and splits at commas; strips initial and trailing
    # whitespace. If user provided only two arguments, "0" will default to
    # list[2]
    split_list= string_input.split(',')
    user_input = [item.strip() for item in split_list]

    while len(user_input) < 3:
        user_input.append("None")
    return user_input


def display_todo(input_dict):
    # Prints a chart of todo items and adds numeric indices.
    i = 1
    print("\n" * 16)
    for key, item in input_dict.items():
        mid_length = 60 - len(key) - len(str(item['Priority']))
        line = (" %s " % ("-" * mid_length))
        print("[%s] %s %s  Priority: %s"  % (i, key, line, item['Priority']))
        i += 1


def main():

    # opens JSON file. Change 'index.json' to a given path if you do not wish
    # to store the file with the script.

    with open('/usr/local/bin/todo_index.json', 'r') as infile:
        JSON_dict = json.load(infile)

    working_dict = todo_dict(JSON_dict)
    working_list = working_dict.convert_to_list()
    run_program = False

    parser = argparse.ArgumentParser()

    parser.add_argument('-a', nargs = 2, help="Adds an item to your todo list. Requires item name and 'priority'")
    parser.add_argument('-d', nargs = 1, help='Deletes an item to your todo list')
    parser.add_argument('-l', action = 'store_true', help='Displays your todo list')
    parser.add_argument('-run', action = 'store_true', help='Runs program in real time')
    parser.add_argument('-rm', action = 'store_true', help='Erases todo list')
    parser.add_argument('-s', action = 'store_true', help='Sorts list by priority')

    parsed_input = parser.parse_args()

    if parsed_input.run == True:
        run_program = True

    elif parsed_input.a:
        working_dict.add_item(parsed_input.a[0], parsed_input.a[1])

    elif parsed_input.d:
        working_dict.del_item(parsed_input.d[0], working_list)

    elif parsed_input.l:
        working_dict.get_dict()

    elif parsed_input.rm:
        working_dict.reset_dict()

    elif parsed_input.s:
        working_dict.sort_priority()

    else:
        print('Something went wrong.')

    # This assures information is only written to JSON file if -run was not
    # selected
    if parsed_input.run == False:
        write_JSON(working_dict.get_dict()) #writes data to JSON file
        display_todo(working_dict.get_dict()) #displays updated todo list


    while run_program == True:

        # opens JSON file. Change 'index.json' to a given path if you do not
        # wish to store the file with the script.

        with open('/usr/local/bin/todo_index.json', 'r') as infile:
            JSON_dict = json.load(infile)

        # creates a todo_dict instance from index.json data
        working_dict = todo_dict(JSON_dict)

        # creates a list that is used to access dictionary items (keys) by
        # number
        working_list = working_dict.convert_to_list()

        # prints a todo list chart
        display_todo(working_dict.get_dict())

        user_input = input("\nEnter a Todo item. Specify 'add item' (-a), 'delete item' (-d), 'list items' (-l), 'sort items' (-s). To add a priority separate the item and priority number with a comma.\n\n")

        if user_input == '-q':
            quit()

        else:
            prepared_input = prepare_input(user_input)

            user_flag = prepared_input[0]
            user_todo_item = prepared_input[1]
            user_todo_priority = prepared_input[2]

        # Dictionary of flags and corresponding method objects. The if, elif,
        # else statements below check the flag_map dictionary and call the
        # given method.

        flag_map = {
        '-a': working_dict.add_item,
        '-d': working_dict.del_item,
        '-l': working_dict.get_dict,
        '-rm': working_dict.reset_dict,
        '-s': working_dict.sort_priority}

        if user_flag not in flag_map:
            input("no valid command was entered. Press any key to continue.")

        elif flag_map[user_flag] ==  working_dict.add_item:
            working_dict.add_item(user_todo_item, user_todo_priority)

        elif flag_map[user_flag] ==  working_dict.del_item:
            working_dict.del_item(user_todo_item, working_list)

        elif flag_map[user_flag] ==  working_dict.get_dict:
            working_dict.get_dict()

        elif flag_map[user_flag] ==  working_dict.reset_dict:
            working_dict.reset_dict()

        else:
            flag_map[user_flag] == working_dict.sort_priority
            working_dict.sort_priority()

        write_JSON(working_dict.get_dict())


if __name__ == "__main__":
    main()
