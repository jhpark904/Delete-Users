# PROGRAMMING ASSIGNMENT 06
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def main():
    """The program does the following:
    1) asks the user to input 5 usernames (only alphanumeric characters will be input,
       no space, no underscore, ...) and stores them into a list
    2) prints out the list of usernames
    3) calls clean_users function to clean the list
    4) prints out the cleaned list"""
    #WRITE YOUR PROGRAM HERE
    usernames = []
    for i in range(5):
        name = input("username: ")
        usernames.append(name)
    print(usernames)
    final_names = clean_users(usernames)
    print(final_names)
    
    


def clean_users(L):
    """• input: 1 parameter L -> type list (of strings) - each element in the list is a username
• return: a new cleaned list (see the rules below) -> type list (of strings)

The logic for cleaning the list of usernames is:
    • if the username contains c, g or z, it should be removed (the same with C, G or Z)
    • otherwise, keep it in the list

Note: your function should not modify the original list!"""
    #WRITE YOUR CODE HERE
    L2 = L[:] # make a clone
    for name in L: #repetition over the original list so the shift of index does not occur when I'm modifying the clone
        if name.lower().find('c') != -1 or name.lower().find('g') != -1 or name.lower().find('z') != -1: # convert the names to lowercase so the search is case insensitive
            L2.remove(name)
    return L2
    


#Call the main() function
main()
