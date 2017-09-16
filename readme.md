#Terminal Todo 


This command line program allows a user to interact with a todo list within the terminal. Data is saved in json format in the same location as the todo.py. 

The user can either interact with the list at the command line either persistently or intermittently, e.g., run the application everytime he/she wants to add/delete an item vs. keeping it running via the ```-run``` command.

## Commands / Flags
* ```-a``` Adds an item to the list. Accepts 2 arguments, the item and the priority.
* ```-d``` Deletes an item from the list. Accepts 1 argument, either the name of the item being deleted or its index as printed by ```-l```.
* ```-l``` Prints the list
* ```-s``` Sorts the list by priority
* ```-rm``` Deletes the entire list

## Modes
The two modes operate slightly different and both have advantages. Both modes accept the same commands, but they function slightly differently.

### Live Mode
In live mode, arguments must be separated by comma and priority is not required (defaults to ```None```). Input can be written with spaces without escaping characters.

To add an item the following would be entered:

```-a, Watch Game of Thrones, 2``` or simply

```-a, Watch Game of Thrones```

### Command Mode
Command mode functions as expected for a terminal. Commas do not separate arguments, and all arguments are required (e.g, ```-a``` requires two arguments and throws an error if only one is given). Spaces and special characters must be escaped to avoid incorrect separation of arguments, or, alternatively, longer entries can be easily surrounded by quotes to avoid escaping characters.

```-a Watch\ Game\ of\ Thrones 2``` or

```-a "Watch Game of Thrones" 2```

Notice the *Priority* argument ```2``` is required from the terminal command line.