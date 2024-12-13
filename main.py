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
    print(" ")
    

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
            return user_input
        user_input = input("That isn't a vaild option. Please try again: ")
        
def view_list(todo_list):
    index = 1
    for item in todo_list:
        print(f"{index}: {item}")
        index += 1

def add_to_list(todo_list):
    item = input("What item would you like to add to your todo list: ")
    todo_list.append(item)
    
def delete_from_list(todo_list):
    index = input("What's the index of the element you're deleting: ")
    todo_list.pop(int(index) - 1)

def edit_list(todo_list):
    index = input("What's the index of the element you're editing: ")
    new_element = input("What are you changing it to: ")
    todo_list[int(index) - 1] = new_element

def main():
    todo_list = []
    while True:
        option = get_user_input()
        print(f"option {option}")
        match (option):
            case "1":
                view_list(todo_list)
            case "2":
                add_to_list(todo_list)
            case "3":
                delete_from_list(todo_list)
            case "4":
                edit_list(todo_list)
            case "5":
                return
            case _:
                print("unknown case")
        

if (__name__ == "__main__"):
    main()