## Overview

**Command Line TODO List**:

**Project Description**:

This is a TODO List that can be run in the command line.
It connects to a Firebase database to store the user's todo list.
This way the todo list will be stored between instances of the program.

**Project Goals**:

The goal of this project was for me to get familiar with Firestore and Firebase.
Additionaly I was just trying to figure out how to use databases in general.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Clone the repo
2. Go to Firebase and make an account or sign in
3. Inside Firebase create a Firestore project and get an adminsdk.json file
4. Paste the adminsdk.json file into the repo and change the import statement in main.py to properly import it
5. Run the python file

Instructions for using the software:

1. Run the program
2. Type the number of the option you'd like to take
3. Repeat until you pick option 6 which exits the program

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

Any Version of the following is okay:

- VSCodium
- Python
- Black

## Useful Websites to Learn More

The only resource I used was the [Official Documentation](https://firebase.google.com/docs)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

- [ ] Add user authentication so multiple people can use the software
- [ ] Add a GUI
- [ ] Add the ability to sort the list
