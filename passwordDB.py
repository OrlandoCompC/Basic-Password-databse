#Developed by Orlando Companioni
#  This program uses a dictionary to perform password operations
# userid and password

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    # create an empty dictionary.
    passwords = {}
    #passwords = dict()
    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # Get the user's menu choice
        choice = get_choice()

        # process the choice
        if choice == LOOK_UP: # Look up a password
            look_up(passwords)
        elif choice == ADD:
            add(passwords) # Add a password
        elif choice == CHANGE:
            change(passwords) # Change a password
        elif choice == DELETE:
            delete(passwords) # Delete a password



def get_choice(): # This function will display the menu and get the user's choice
    print()
    print("Password database operations")
    print("1. Look up the password database")
    print("2. Add a password to database")
    print("3. Change a password")
    print("4. Delete a password")
    print("5. Quit the program")
    print()
    
    # Get a user choice 
    choice = int(input("Enter your choice "))
    # validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))
    
    return choice # returns the choice to the user
    
# The look_up() funciton looks up a password in the passwords dictionary
def look_up(passwords):
    # Get a userid from the user
    userid = input("Enter the user ID: ")
    print(passwords.get(userid, 'User ID not found')) # Look it up in the passwords dictionary

# The add function will add a new entry to the passwords dictionary
def add(passwords):
    # Get a new username and password from the user
    userid = input("Enter user ID: ")
    pwd = input("Enter user password: ")

    # If userid doesn't exist in the dictionary, add it
    if userid not in passwords:
        passwords.update({userid:pwd})  # Add the user ID and password to the dictionary
        print("Adding the password to the database")
    else:
        print("The userID already taken!") # If the user ID is already in the dictionary


def change(passwords): # This function will change the password of a user
    userid=input("Enter the user ID: ")
    if userid in passwords: # If the user ID is in the dictionary
        pwd=input("Please enter the new password: ")
        passwords[userid]=pwd
        print("The Password has been updated")
    else:
        print(f"The userID does not exist, Please make one")

def delete(passwords): # This function will delete a user from the dictionary
    userid=input("Please enter the userID you would like to delete: ")
    if userid in passwords: # If the user ID is in the dictionary
        del passwords[userid] # Delete the user ID
        print("The user has been deleted from the program")
    else:
        print("User ID not found") # If the user ID is not in the dictionary

    

    
if __name__ == '__main__':
    main()



        
