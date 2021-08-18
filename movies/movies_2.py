#
# A bit more elaboration of movies
# 
# Why have the code in a function. Lets abstract thecode so it is
# generalised and re-usable

def process_prices( price_type ):
    # define variables for the cost of tickets
    adult_ticket_cost = 18
    child_ticket_cost = 10

    print('Welcome to the ' + price_type + ' price calculator!\n\nHow many tickets do you require?\n\n')

    # a simple use of input - there is no validation though so this isn't 
    # nearly sufficient in the real world
    adult_count = int(input('How many adults? '))
    child_count = int(input('How many children? '))

    total_cost = adult_ticket_cost * adult_count + child_ticket_cost * child_count

    # __repr__ is a special thing in python which returns a string representation
    # of an object but you can't rely on what is returned being a simple string if
    #  the object is a complex object
    print('\n\nTotal cost to take your family to the '  + price_type + ': ' + total_cost.__repr__())


process_prices('movies')
process_prices('fair')