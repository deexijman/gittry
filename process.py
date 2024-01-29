# processing a json response in python

# using classes and conditionals

class Process: # user defined data structure

    # data members and member functions definition
    TimeOfResolution =  [] # stack to store all requests
    ApiResolveHistory = {} # store all request history
    ApiLink = ''

    # member functions
    def __init__(self, ApiLink : str):
        self.ApiLink = ApiLink

    
        

