###############################################################################
###############################################################################
#
# input_0
#
# input_0 is a module which contains a shared implementation of the
# get_menu_selection function
#
#
###############################################################################
###############################################################################


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
    # this is the same thing twice done in different ways - the enabled
    # one is simpler to explain but the other is more advanced - see if you
    # can research and undestand how the other works.
    # ERROR = "Please enter a number between {} and {}\n".format(low,high)    
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