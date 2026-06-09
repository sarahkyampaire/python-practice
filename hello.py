# 1. Ask the user for two numbers
number_one = float(input("Enter your first number: "))
number_two = float(input("Enter your second number: "))

# 2. Perform basic calculations
addition = number_one + number_two
subtraction = number_one - number_two
multiplication = number_one * number_two

# 3. Print the results out to the screen
print("\n--- CALCULATOR RESULTS ---")
print("Addition Result:       ", addition)
print("Subtraction Result:    ", subtraction)
print("Multiplication Result: ", multiplication)
#understanding global variables
name="julius"
def greet():
    print("hello",name)
greet()
#another global variable
cow="fresian"
def type():
    print("the cow is a",cow)
type()
company_name="Uganda Breweries"
def name():
    print(f"The girl works at {company_name}")
name()
company_name="MTN"
def show_company():
    print(f"i work at Uganda {company_name}")
show_company()
#A function that is a currency converter.
Exchange_Rate=3570  #1USD to UGX
def exchange(Amount_in_USD):
    TOTAL=Amount_in_USD*Exchange_Rate
    print(f"{Amount_in_USD} USD is {TOTAL}")
exchange(10000)
status="married"
def show_status():
    print(f"The lady is presently {status}")
show_status()
#Another example where we use the if statement
Is_admin="True"
def grant_permission():
    if Is_admin:
        print(f"Access granted")
    else:
        print(f"Access denied")
grant_permission()
Is_admin="False"
def grant_permission():
    if Is_admin:
        print(f"access denied")
    else:
        print(f"access granted")
grant_permission()
#Using a local variable to override a global variable
Login_count=0
def count_logins():
    global Login_count
    Login_count+=1
    print(f"Total logins is {Login_count}")
count_logins()
count_logins()
count_logins()
count_logins()
#light switch moment
Is_Light_On=False
def Light_Switch():
    global Is_Light_On
    if Is_Light_On==False:
        Is_Light_On=True
        print(f"The light is now ON")
    else:
        Is_Light_On=False
        print(f"The light is now OFF")
Light_Switch()
Light_Switch()
Light_Switch()
#store status
Store_Status="closed"
def status():
    global Store_Status
    if Store_Status=="closed":
        Store_Status="open"
        print(f"we are ready to serve")
    else:
        Store_Status="closed"
        print(f"Not available today")
status()
status()
#Another store incident
Is_Store_Open="True"
def Store_Status():
    if Is_Store_Open==True:
        print(f"Available today")
    else:
        print(f"we are sorry")
def Close_Store():
    global Is_Store_Open
    Is_Store_Open="False"
    if Is_Store_Open=="True":
        print(f"we are closing right now")
    else:
        print(f"closed")
Store_Status()
Close_Store()
#Another example
Is_Class_Open="False"
def Open_Class():
    if Is_Class_Open=="True":
        print(f"Its open")
    else:
        print(f"We are closed")
def New_Status():
    global Is_Class_Open
    if Is_Class_Open=="False":
        Is_Class_Open="True"
        print(f"We are now fully open")
    else:
        print(f"we are closed")
Open_Class()
New_Status()
#Permission store.
Is_admin="True"
def User_Role():
    if Is_admin=="True":
        print(f"permission granted")
    else:
        print(f"permission not granted")
def Use_Database():
    global Is_admin
    if Is_admin=="True":
        Is_admin="True"
        print(f"Access to database granted")
    else:
        print(f"Access to database denied")
def Login_As_Admin():
    global Is_admin
    if Is_admin=="True":
        Is_admin="True"
        print(f"Access granted")
    else:
        print("Access denied")
User_Role()
Login_As_Admin()
Use_Database()






