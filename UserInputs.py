name=input("What is your name?")
print(f"my name is {name}")
print(f"its nice to meet you {name}")
#converting string numbers to integer numbers
Age=input("How old are you")
Age=int(Age)
Future_Age=Age+1
print(f"A year from now,you will be {Future_Age}years old")
#Writing a short function
Price=input("what is the price of one goat?")
Price=int(Price)
Quantity=input("How many goats do you want to buy")
Quantity=int(Quantity)
Total_Price=Price*Quantity
print(f"This will cost you {Total_Price} shillings" )
#Using the except function to overcome input errors.
try:
    Age=int(input("How old are you?"))
    Future_Age=Age+2
    print(f"you will be {Future_Age} old in the next two years")
except ValueError:
    print("Enter a valid number")
    input("How old are you now?")
    print(f"You will be {Future_Age} years soon")
    #Using Split()
Data=input("Enter three numbers separated by comas:")
numbers=Data.split(",")
print(f"The values are{numbers}")
x,y,z=map(int,numbers)
print(f"The sum is {x+y+z}")
#Quiz:code that cleans,excepts and prints
figures=input("Enter the numbers you have separated by commas:")
Real_figures=figures.split(",")
a,b,c=map(int,Real_figures)
sum=a+b+c
print(f"The total amount is now{sum}")
try:
    Names=input("Enter your names separated by commas:")
except:ValueError
input("Enter valid Names separated by commas:")
Names=Names.upper()
Names=Names.split(",")
print(f"Your true names are{Names}")
age=input("How old are you now?:")
age=int(age)
Future_Age=age+10
print(f"You will be {Future_Age} in ten years")
confirm=input(str("Would you like to save your progress?Yes/No:"))
if confirm=="No":
    print(confirm.upper())
    print("Not saved")
else:
    print("progress saved")
#short time programs
cat_sound="moew"
dog_sound="bark"
def animal_sound(sound):
    if sound=="cat_sound":
        print("That a cat making sound")
    elif sound=="dog_sound":
        print("Thats the sound of a dog")
    else:
        print("The sound is not known")
animal_sound(cat_sound)
animal_sound(dog_sound)
#just modifying code
    


    


    




