# Tab constant to be used throughout the program
TAB = " " * 4

def print_options():
    """Prints a list of options to the command line"""
    print("What action would you like to take?")
    print(f"{TAB}1. View List")
    print(f"{TAB}2. Add Item to List")
    print(f"{TAB}3. Delete Item from List")
    print(f"{TAB}4. Edit Item on List")
    print(f"{TAB}5. Exit Program")
    

def get_user_input():
    """Ask the user for input until they provid a vaild input."""
    
    valid_options = [
        "1",
        "2",
        "3",
        "4",
        "5"
    ]

    print_options()
    user_input = input("Type number of selected option: ")
    
    while True:
        if user_input in valid_options:
            return valid_options
        user_input = input("That isn't a vaild option. Please try again: ")


def main():
    todo_list = []
    while True:
        option = get_user_input()
        break
        

if (__name__ == "__main__"):
    main()