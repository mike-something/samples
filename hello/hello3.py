
# declaration of nice message
def niceMessage():
    # Comment and uncomment next line to see the impact of global variable scope.
    # When global is commented the message variable in nice message is only used
    # in niceMessage. When global scope is declared message will be in effect at
    # the program level and overwrite the prior definition of message
    # global message
    message = "It's a lovely day"
    print(message)
    input('Press any key to continue')


# declaration of nastyMessage
def nastyMessage():
    print('Second ', message)
    input('Press any key to continue')


# define a top level message at program scope
message = 'Old toe rag'
print('Program scope ', message)
# invoke\run\call niceMessage
niceMessage()
# invoke\run\call nastyMessage
nastyMessage()


input('Press any key to exit program')

