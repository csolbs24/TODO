import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

cred = credentials.Certificate(
    "todo-list-cse310-firebase-adminsdk-jmntb-4ad8b50f00.json"
)
firebase_admin.initialize_app(cred)

db = firestore.client()  # Create a Firestore client

# Cloud Firestore
items_ref = db.collection("items")


# Tab constant to be used throughout the program
TAB = " " * 4


def write_to_db(todo_list):
    """Write the given todo list to the database"""
    db.document("items/user").set({"items": todo_list})


def print_options():
    """Prints a list of options to the command line"""
    print("What action would you like to take?")
    print(f"{TAB}1. View List")
    print(f"{TAB}2. Add Item to List")
    print(f"{TAB}3. Delete Item from List")
    print(f"{TAB}4. Edit Item on List")
    print(f"{TAB}5. Delete Entire List")
    print(f"{TAB}6. Exit Program")
    print(" ")


def get_user_input():
    """Ask the user for input until they provid a vaild input."""

    valid_options = ["1", "2", "3", "4", "5", "6"]

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
    print()


def add_to_list(todo_list):
    item = input("What item would you like to add to your todo list: ")
    view_list(todo_list)
    todo_list.append(item)
    write_to_db(todo_list)


def delete_from_list(todo_list):
    index = input("What's the index of the element you're deleting: ")
    view_list(todo_list)
    todo_list.pop(int(index) - 1)
    write_to_db(todo_list)


def edit_list(todo_list):
    index = input("What's the index of the element you're editing: ")
    new_element = input("What are you changing it to: ")
    view_list(todo_list)
    todo_list[int(index) - 1] = new_element
    write_to_db(todo_list)


def delete_everything(todo_list):
    """Make a database request to delete everything in the list"""
    todo_list = []
    write_to_db([])


def main():
    # Grab the todo items from the database
    items = items_ref.stream()

    # Populate the local todo list with the db items
    todo_list = None
    for item in items:
        todo_list = item.to_dict()["items"]  # The list is stored as the items property
    if todo_list is None:
        todo_list = []

    # Continually loop until the user exits
    while True:
        option = get_user_input()
        print()
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
                delete_everything()
            case "6":
                return
            case _:
                print("unknown case")


if __name__ == "__main__":
    main()
