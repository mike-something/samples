# PART 2 - this tutorial continues where Tutorial 18a finished off. Def (below) stands for define.

import sys

def mainMenu():   # this code is defining a function
    
    while True:  # a while loop inside the main-menu function, (2 layers on indent) each time the user makes a selction and performs a task, the menu will pop back up again,
        print ()
        print('''### SHOPPING LIST ###

        Select a number for the action that you would like to do:

        1. View shopping list
        2. Add item to shopping list
        3. Remove item from shopping list
        4. Chck if item is on shopping list
        5. How many items on shopping list
        6. Clear shopping list
        7. Exit
        ''')


        selection = input("Make your selection: ")

        if selection == "1": 
            displayList()
        elif selection == "2":
            addItem()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            pass
        elif selection == "5":
            pass
        elif selection == "6":
            pass
        elif selection == "7":
            sys.exit()   

        else:
            print("You did not make a valid selection.")


shopping_list = ["apples", "bananas", "carrots", "potatoes"]

def displayList(): # this function is called "display list" Inside this function a code is written below to make the shopping list appear on the screen.
    print()
    print("---SHOPPING LIST===")
    for i in shopping_list:   # variable i is set to the first item in the shopping list, which is apples. The code loops back around and is set to the second item - bananas, and loops back around to carrots and the same for potatoes. When it gets to the end of the loop, it realises that there's no more words to be displayed, so jumps out of the loop and processes any code beneath it.
        print("* "+ i) # this code will print out an asterix first and then it will put whatever work i is equal to, eg apples, oranges....


def addItem():
    item = input("Enter the item you wish to add to the shopping list: ")
    shopping_list.append(item) #this accesses the shopping list and places an item into the list.
    print(item + " has been added to the shopping list.")

def removeItem():
    item = input("Enter the item you wish to remove from the shopping list: ")
    shopping_list.remove(item) #this accesses the shopping list and places an item into the list.
    print(item + " has been removed from the shopping list.")

    
mainMenu()  # when the computer sees this, it has to go back up the top of the code and (all the code which is indented is









