#
# A more elaborated example
# 
# Lets add more parameters to the function and return a value
# so we can calculate the total cost of the day out

def process_prices( price_type, adult_ticket_cost, child_ticket_cost ):


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