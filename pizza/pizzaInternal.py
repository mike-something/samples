def functionOutput(pizza):
    i =0
    print("=================================================")
    print("Pizza Ordering System")
    print("=================================================")
    print("Code   Item                Price   Number Ordered")
    while i < len(pizza):
        print(pizza[i].ljust(6),pizza[i+1].ljust(20),str(pizza[i+2]).ljust(9),str(pizza[i+3]).ljust(5))
        i=i+4

def functionOrderType(): #this function ask for the customer's name, and asks if the order will be delivered or not, if it is delivered it will ask for the user's address, phone number.
     global delivery
     global address
     global name
     global contact_number
     delivery=False
     name=input("What is you name? (Press 'C' or 'c' to cancel)") #asks for name,and if the user wants to cancel the program
     if name=="C" or name=="c": #if the user types in C or c the program stops
        functionExit()
     order_type=input("Are you wanting this order to be delivered? (Press D or d)  or will you be picking it up from your nearest store? (please press any other letter) or (press C or c) to cancel: ")
     if order_type=="C" or order_type=="c":
        functionExit()
     if order_type=="D" or order_type=="d":
        delivery=True
        address=input("Please type the address of where you would like your pizza delivered to: ") # asks the user to where they want the pizza to be ordered
        contact_number=input("Please type in your phone number: ")# asks the user their phone number so that they can contact him/her
        print("A Delivery Charge of $3 will be added to your order total")
     functionEdit(pizza) #calls out functionEdit

def functionEdit(pizza): # this function asks the user how many pizzas they would like to order and what kind of pizzas
    global pizza_quantity 
    pizza_quantity=0
    order_completed=False
    while order_completed==False:
        check_num=False
        while check_num==False:
            try:
                pizza_quantity=int(input("How many pizzas would you like to order?"))
                if pizza_quantity not in range(1,6):#error traps if the user types in a number below 0 or above 5
                    print("Sorry, you can only order up to 5 pizzas!")
                else:
                    check_num=True
            except ValueError:# error traps if the user types in an invalid code i.e. a letter
                print("You have entered an invalid code - please try again")
        for counter in range(pizza_quantity): #ask for the code number as many times as what the user inputed in the number of pizza they want to order
            check_code=False
            while check_code==False:
                    code=input("Please enter the Code number of the pizza you want to order: ")
                    if code in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
                        codeno=int(code)#this changes the string to an integer so calculations can be done if needed
                        pizza[4*codeno-1]=1
                        check_code=True
                    else:
                        print("You have entered an invalid code - please try again")
                        order_completed=True
        functionProcessOrder()

def functionProcessOrder(): # this function calculates the total amount of the order
    n = 0
    i=0
    global cost
    cost = 0
    delivery_charge=3
    print("=================================================") #starts the table
    print("Pizza Ordering System")
    print("=================================================")
    print("Code   Item                Price   Number Ordered")
    while i < (len(pizza)):
        check = (pizza[n])
        if check != 0:
            print(pizza[i].ljust(6),pizza[i+1].ljust(20),str(pizza[i+2]).ljust(9),str(pizza[i+3]).rjust(5))
            cost=cost+float(pizza[i+2])*float(pizza[i+3]) #makes the table format
        i=i+4
        n=n+4
    if delivery:
        cost=cost+delivery_charge
        print("The total of your order including delivery charge of $3 is $"+str(round(cost,2)))#calcalculates the total cost of the order with the delivery charge
        print("This order will be delivered at: ",str(address))
        print("The phone number we will contact you by is: ",str(contact_number))
    else:
        print("The total of your order is $"+str(round(cost,2)))#calculates the total cost of the order without the delivery charge
        print("Your order will be ready for pickup in 15 minutes")
    continue_program=input("Do you wish to get another order or finish? If you wish to finish press F or any other key to continue") # ask the user if they want to order again or quits the program
    if continue_program=="F": # if "F" is clicked the program
        functionExit()
    else:
        functionOrderPizza()


def functionExit(): # this function prints a Thank You message
    print("Thank you. Have a good day and enjoy your pizza(s)!.")
    exit()

def functionOrderPizza():# this function calls out functionOutput() and functionOrderType()
    functionOutput(pizza)
    functionOrderType()
    pizza=[
        '1','Classic',7.50,0,
        '2','Hawaiiwan',8.50,0,
        '3','Pepperoni',8.50,0,
        '4','Ham and Cheese',8.50,0,
        '5','Chicken',8.50,0,
        '6','Cheese and mushroom',8.50,0,
        '7','Margherita',8.50,0,
        '8','Garlic',8.50,0,
        '9','Meat Lovers',13.50,0,
        '10','Super Supreme',13.50,0,
        '11','Seafood',13.50,0,
        '12','Pesto',13.50,0]

#main routine



functionOrderPizza()

print( delivery, address, name, contact_number )

    
