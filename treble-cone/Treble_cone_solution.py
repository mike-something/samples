# if you need to import modules or libraries it is done here e.g.
# import somelibraryname

###############################################################################
#
# global variables definitions
#
###############################################################################

# define a list with the types of equipment available
GEAR = ["Skis", "Boots", "Poles", "Snowboard", "Jacket", "Pants", "Gloves"]

# define a list with the cost of equipment - this has the 
# same number of items as GEAR and we are just referencing 
# prices by the index in the array
GEAR_PRICES = [15, 10, 5, 15, 5, 5, 5]

# define a list of pass prices
PASS_PRICES = [135, 68]

# define an empty list which we will add to as the user selects gear to hire
hiredGear = []


###############################################################################
###############################################################################
#
# get_menu_selection()
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
    ERROR = "Please enter a number between {} and {}\n".format(low,high)

    while True:
        try:
            number = int(input(question))

            if number >= low and number <= high:
                return number
            else:
                print(ERROR)

        except:
            print(ERROR)


###############################################################################
###############################################################################
#
# hire_gear()
#
# function which controls the gear hiring process specifically
#
# Input Parameters: none
#
###############################################################################
def hire_gear():
    global hiredGear
    menu = "Select which gear you need to hire:\n"

    # iterate through the gear options and display the menu selection 
    # for each item
    option = 1    
    for gear_item  in GEAR:
        menu += str(option) + ". " + gear_item + "\n"
        option += 1

    while True:

        gearIndex = get_menu_selection(menu, 1,len(GEAR))
        print()

        if (gearIndex in hiredGear):
            print("You have already chosen this item\n")
        else:
            return gearIndex - 1


###############################################################################
###############################################################################
#
# calculate_cost()
#
# calculate the costs of bookings
#
# CLASS TASK - develop good comments for what the below parameters are
# Input Parameters:
#    num_a - ???
#    num_c - ???
#
# references global hiredGear list variable
#
###############################################################################
def calculate_cost(num_a, num_c):
    bill = "------- Ski Pass Bill -------\n" \
           "Adult passes:\t\t\t$"+str(num_a*PASS_PRICES[0])+\
           "\nChildren Passes:\t\t$"+str(num_c*PASS_PRICES[1])+\
           "\n -- Hired Gear --\n"

    total_gear_cost = 0

    # iterate through hiredGear extracting the stored selections and calculate cost
    for each_hired_gear in hiredGear:
        if each_hired_gear == 3:
            bill += GEAR[each_hired_gear] +"\t\t\t$"+str(GEAR_PRICES[each_hired_gear]*(num_a+num_c))+"\n"
        else:
            bill += GEAR[each_hired_gear] +"\t\t\t\t$"+str(GEAR_PRICES[each_hired_gear]*(num_a+num_c))+"\n"
        total_gear_cost += GEAR_PRICES[each_hired_gear]*(num_a+num_c)

    bill += "\nTotal Gear Cost:\t\t$"+str(total_gear_cost)+"\n"+("-"*29)+"\nTOTAL COST:\t\t\t\t$"+str((num_a*PASS_PRICES[0])+(num_c*PASS_PRICES[1])+total_gear_cost)+"\n"+("-"*29)

    print(bill)
    print()


###############################################################################
###############################################################################
#
# process_booking()
#
# a function which processes bookings. To do this it;
#
# 1. prompts to define the number of adults
# 2. prompts to define the number of children
# 3. prompts to select the gear to hire via a call to hire_gear
# 4. calculates and prints costs via call to calculate_cost
#
# references global hiredGear list variable
#
###############################################################################
def process_booking():
    global hiredGear

    # local variables
    num_adults = 0
    num_children = 0

    define_adult_count = True
    while define_adult_count:

        num_adults = get_menu_selection("Enter the number of adults:\n", 0, 50)

        if num_adults == 0:
            print("There need to be at least one adult")
            print()
        else:
            define_adult_count = False

    num_children = get_menu_selection("Enter the number of children:\n", 0, 50)
    print()

    equipment_selection = True
    while equipment_selection:

        # call the function hire_gear within the append operation for 
        # hire gear. This could also be expressed as e.g.;
        #
        # gear_definition = hire_gear()
        # hiredGear.append(gear_definition)
        #
        hiredGear.append( hire_gear() )

        gear_choice = get_menu_selection("Would you like to hire other gear?\n1. Yes\n2. No\n", 1, 2)
        print()

        if gear_choice == 2:
            equipment_selection = False

    calculate_cost(num_adults, num_children)


###############################################################################
###############################################################################
#
# main process begins here - the python compiler will have parsed and loaded 
# the global variables and function definitions defined above so we can enter 
# the program logic.
# 
# A simple top level loop keeps processing new hires until the user selects
# the option to not make another booking
#
###############################################################################
print(("%"*35)+"\nWelcome to Treble Cone Booking App\n"+("%"*35)+"\n")

continue_booking = True

while continue_booking:

    process_booking()

    user_choice = get_menu_selection("Would you like to make another booking?\n1. Yes\n2. No\n", 1,2)
    print()

    if user_choice == 2:
        continue_booking = False

print("Thank you for your booking!")
