"""
After the user has entered valid credentials 
1. Store the credentials in a dictionary called database which has the values 
	database = {
		username : [
		user_balance , username
	]
}

2. we get the username they entered by using the .get method for dictionaries e.g 
	if username!="":
		database.get(username , 'Invalid username') - output [inside of .get the left hand value
														is for getting the key and the right hand
														value if the exception/ error message if the
														user does not exist
																	]
	if their credential checkout then we should get from the dictionary a list with bank balance and their
	username. We can use indexes to get the balance and username for dashboard e.g f"welcome {database.get(username)[0]}"
3.  incase the user is not registred we call out signup() function to make them signup
	after the we call the login() after we have stored the values in the database

4. After the sucessful login we run our while loop until the user chooses to logout 
"""

database: dict = {"Juniorzwane": ["1234" ,5000]}


def dashboard(username):
    balance = database.get(username)[
        1
    ]  # assign the balance to a variable for easier access
    # Username is not yet defined because we have to recieve it from login()
    print(
        f"Welcome back to your CodeBank profile {username}\nYour current balance is {balance}\n"
    )
    print("Please make a selection below:\n1.Withdraw\n2.Deposit\n3.LogOut")
    option_Selection = int(
        input("Choose an option above e.g 1 : ")
    )  # input always returns a string so convert to integer using the int function
    while True:
        # if option_Selection == 1:
        # 	print(f'Your balance is : {balance}\n') # on the returned list the 0 index value is balance
        # 	option_Selection = int(input('Choose an option above e.g 1 : '))
        if option_Selection == 1:
            withdraw = int(input("Please enter a withdrawal amount: "))
            if (
                withdraw > balance
            ):  # error handling for instances where the amount entered is greater than the balance
                print("Insufficient funds for the amount selected\n")
            else:
                balance = (
                    balance - withdraw
                )  # updating the balance after withdrawing x amount of money
                print(
                    f"Your remaining balance is : {balance}\nThank you for using CodeBank!\n"
                )  # returning the new balance
                option_Selection = int(input("Choose an option above e.g 1 : "))
        elif option_Selection == 2:
            deposit = int(input("Enter deposit amount : "))
            balance = (
                balance + deposit
            )  # updating the balance after depositing x amount of money
            print(
                f"Your updated balance is : {balance}\nThank you for using CodeBank!\n"
            )
            option_Selection = int(input("Choose an option above e.g 1 : "))
        elif option_Selection == 3:
            print("Thank you for using CodeBank...\nLogging out.")
            break
        else:
            print(f"Please enter a valid input\n")
            option_Selection = int(input("Choose an option above e.g 1 : "))

def register():
    '''
    This fucntion is used to register the user 
    >>> username 
    '''
    return 

def login():
    global username
    username = input("Enter your username ")
    if username in database:
        password = input("Enter your password")
        if(database[username][0] == password):
            dashboard(username)
        else:
            print("Error, incorrect password")
    else:
        print("THe user name does not exist, register for a new account")
        register()
    return username
 
def accessAccount():
    accessAcc = input("Welcome to CodeBank\nWould you like to 'login' or 'register'? ")
    if(accessAcc.lower() == "login"):
        login()
    elif(accessAcc.lower() == "register"):
        register()
    else:
        return print("invalid input")

accessAccount()
