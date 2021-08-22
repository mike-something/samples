

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
            
            number = int(input(question + " "))

            if number >= low and number <= high:
                # return breaks out of the loop, whew - otherwise we might 
                # continue processing forever or until the power goes off
                return number
            else:
                print(prompt)

        except:
            print(prompt)    



def age_entitlements():

    # query and print age related entitlements - the conditions accumulate so 
    # at an older age all prior rights still exist so it could be changed 
    # to be more nuanced
    #
    # the entitlements coudl be stored in a dictionary and looked up so you
    # have a loop rather than a potentially infinitley expanding list of tests
    #
    # this could be changed to query an age category a user falls into
    # 
    user_age = get_menu_selection('How old are you?', 0, 120 )

    if (user_age < 5 ) :
        print("You don't exist yet, sorry but you have no entitlements")
    
    if (user_age >= 5):
        print("Go to school")

    if (user_age >= 14):
        print("Look after children independently")

    if (user_age >= 16):
        print("Get a drivers license")

    if (user_age >= 18):
        print("Vote")            
        print("Leave home")            

    if (user_age >= 65):
        print("Retire and receive a pension from the government")




age_entitlements()    