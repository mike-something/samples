###############################################################################
###############################################################################
# 
# A more elaborated example
# 
# Here we introduce importing a module we will use this in all later examples 
# and elaborate toward demonstrating the value and use of modules. Importantly
# the term module can be used interchangeably with libraries and refers to 
# code which is organised to allow it to be shared and resused by multiple  
# using programs
#
###############################################################################
###############################################################################

# import the sys, pathlib and os modules. We need all these to manipulate
# our environment
import sys
from pathlib import Path
from os import path
#
# This is a bit longer than I would like but it is how you can import a 
# relatively located module - you probably want modules located somewhere where 
# they are accessible to muliple projects see 
# https://fortierq.github.io/python-import/ for more.
#
# See below for more information and explanation of how we do the import for this
# example. It takes a bit of messy code to make imports work for local projects.
#
# This uses the __file__ system variable to get the name of this file and sets 
# references to our modules directory. Our modules directory is assumed to be at
# the same level as the program directory (i.e. one level up from the code itself). 
#
# It is a sad fact of doing programming for more complex scenarios but you end up 
# having to understand managing files and folders and their relative locations. 
# You need to do this in the end for web development too. 
# 
# The path.sep part of creating the module path references the path separator 
# which is "\" on windows and "/" on a Mac and makes sure it will be correct on 
# either system.
#
module_path = str(Path(__file__).parents[1]) + path.sep + "modules"
sys.path.append(str(module_path))
#
# this import style form can be compared to the import in the movies_5b.py file
from input_0 import get_menu_selection


###############################################################################
###############################################################################
#
# process_prices()
#
# a function which presents the user with a menu and checks input to verify the
# user selections
#
# Input Parameters:
#    price_type - a string which is composed to present the user with a 
#                 meaningful message. This is hard to get right for all uses
#                 so some presentations can look a bit odd
#    adult_ticket_cost - a number defining the adult ticket cost
#    child_ticket_cost - a number defining the child ticket cost
#
###############################################################################
def process_prices( price_type, adult_ticket_cost, child_ticket_cost ):


    print('\n\nWelcome to the ' + price_type + ' price calculator!\n\nHow many tickets do you require?\n\n')

    # we use a validation function - this will check input and returns an integer
    # type so we don't need to cast to int any more here either. We want to allow 
    # any size of input so we use system defined maxint instead of defining a 
    # possibly wrong version ourselves
    adult_count = get_menu_selection('How many adults? ', 0, sys.maxsize )
    child_count = get_menu_selection('How many children? ', 0, sys.maxsize )

    total_cost = adult_ticket_cost * adult_count + child_ticket_cost * child_count

    # __repr__ is a special thing in python which returns a string representation
    # of an object but you can't rely on what is returned being a simple string if
    #  the object is a complex object
    print('\n\nTotal cost to take your family to the '  + price_type + ': ' + total_cost.__repr__())

    return total_cost



# define variables for the cost of activities for the day
adult_movie_cost = 18
child_movie_cost = 10
adult_fair_cost = 27
child_fair_cost = 19
adult_sailing_cost = 30
child_sailing_cost = 25

movie_cost = process_prices('movies', adult_movie_cost, child_movie_cost)
fair_cost = process_prices('fair', adult_fair_cost, child_fair_cost)
sailing_cost = process_prices('sailing', adult_sailing_cost, child_sailing_cost)

print('\n\nYour day out will cost ' + str(movie_cost + fair_cost + sailing_cost))