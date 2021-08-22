#
# cut down version for example only - this shows a different way of
# defining module references using 
#
#     import <MODULENAME>
#     rather than
#     from <MODULENAME> import <property or function>
#
# the code is compressed with only the parts which are different
# from movies_5a.py containing comments
# 
#

import sys
from pathlib import Path
from os import path


module_path = str(Path(__file__).resolve().parents[1]) + path.sep + "modules"
sys.path.append(str(module_path))

#
# this import style can be compared to the import in the movies_5a.py file
# note that we need to reference the method differently below too.
# As another note many python environments may flag thids import as an 
# error as python doesn't know about this module until the program is run
# and the lines of code just above this execute
import input_0



def process_prices( price_type, adult_ticket_cost, child_ticket_cost ):
    print('\n\nWelcome to the ' + price_type + ' price calculator!\n\nHow many tickets do you require?\n\n')



    #
    # here we have to reference the specific properties from the module explicitly
    # via the input_0.get_menu_selection way of referencing
    adult_count = input_0.get_menu_selection('How many adults? ', 0, sys.maxsize )
    child_count = input_0.get_menu_selection('How many children? ', 0, sys.maxsize )

    # end of example:
    # you can sefely ignore everything below this 



    total_cost = adult_ticket_cost * adult_count + child_ticket_cost * child_count
    print('\n\nTotal cost to take your family to the '  + price_type + ': ' + total_cost.__repr__())
    return total_cost

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