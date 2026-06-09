try:
     user_details=input("Enter your age:")
     user_details=int(user_details)
     print(f"you are now {user_details} years old")
except ValueError:
     print("write a proper number")
#Removes extra space
state=input("Do you want to save progress? yes/no:").strip().lower()
if state=="yes":
     print("progress saved")
else:
     print("progress not saved")
#coordinate splitter.
coordinates=input("please enter coordinates separated by comas:")
print(coordinates)
new_cordinates=coordinates.split(",")
print(new_cordinates)
#Simple calculater
NUM1=input("Enter a certain number:")
First_Number=int(NUM1)
NUM2=input("Enter another number:")
Second_Number=int(NUM2)
print(f"my first number is {First_Number}")
print(f"my second number is {Second_Number}")
choose_operator=input("choose any of the operators e.g (-,+,*,/):" )
operator="choose_operator"
sum=First_Number+Second_Number
difference=First_Number-Second_Number
product=First_Number*Second_Number
if operator=="+":
     print(f"The sum of the two numbers chosen is:",{sum})
elif operator=="-":
     print(f"The difference of the numbers is:",{difference})
else:
     print(f"The product of the numbers is:",{product})
print(sum)
print(product)
print(difference)




