###############################################################################
###############################################################################
# 
# A more elaborated example
# 
# Lets add more parameters to the function and return a value
# so we can calculate the total cost of the day out
#
# It's about time we looked at validation too so lets move getting
# our input values to a new function
#
# Lets step up our quality of documentation and define really good comments
# for the methods in our code
#
###############################################################################
###############################################################################

# import the sys module - we will use a property of that. You don't need to but
# it is good to define your imports in a single place
import sys


###############################################################################
###############################################################################
#
# get_menu_selection()
#
# You'll recognise me from the treble cone example - there is a better way to 
# share code than this which we will deal with in a later elaboration
#
# a function which presents the user with a menu and checks input to verify the
# user selections
#
# Input Parameters:
#    question - a string defining the question which will be presented to the 
#               user
#    low - a number defining the lowest valid value in the selection range
#    high - a number defining the highest valid value in the selection range
#
###############################################################################
def get_menu_selection(question, low, high):

    # define a string variable with the error message we will print
    prompt = "Please enter a number between " + str(low) + " and " + str(high) + "\n"

    # this means the loop will never exit unless a later
    # test breaks out of the loop
    while True:
        try:
            
            number = int(input(question))

            if number >= low and number <= high:
                # return breaks out of the loop, whew - otherwise we might 
                # continue processing forever or until the power goes off
                return number
            else:
                print(prompt)

        except:
            print(prompt)    


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