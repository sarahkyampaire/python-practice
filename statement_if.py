age=input("Enter your age:")
age=int(age)
print(f"you are {age} years old")
if age>=18:
    print("you are an adult")
elif age>10 and age<18:
    print("You are a teenager")
else:
    print("you are a child")
for i in range(5):
    print(i)
    i=i+1

#Asks a user for a number and then prints the multiplication table.
number=input("Enter a number of your choice:")
number=int(number)
print(f"Your number of choice is:{number}")
print("here is the multiplication table")
for i in range(1,10):
    result=number*i
    print(f"{number}*{i}={result}")
#for loop in a list
My_goals=["health","wealth","family"]
for goal in My_goals:
    print(f"Resolution:{goal} Goal")
#List filter
List2=[12,54,10,64,2,30,20,51] 
List3=[]
for i in List2:
    if i>50:
        List3.append(i)
print(List3)
#List of daily temperatures
Temperature=[10,15,30,28,23,40,16,41]
for temperature in Temperature:
    if temperature>=30:
       print(f"its a hot day.temperatures are:{temperature}")
    else:
        print(f"its a pleasant day,temperatures are:{temperature}")
#while loop
count=5
while count>0:
    print(count)
    count=count-1
#Guess the number
Number=input("Enter a number of your choice:")
Number=int(Number)
while Number!=15:
    Number=int(input("wrong number.Try again:"))
    print(f"yes {Number} this is the number we are looking for")
    Number=Number+1
    break;
#Simple while loop.printing numbers from 1 to 10.
number=1
while number<=10:
    print(number)
    number=number+1
#ATM PIN checker.
User_Pin=2025
Entered_Pin=""
Entered_Pin=input("Enter a user pin:")
while Entered_Pin!=User_Pin:
    input("You entered a wrong pin,try again:")
    break;
print("thats true pin,Access granted")
#count from 1 to 10
number=1
while number<=5:
    print(number)
    number=number+1
#ask for password until correct.
Right_pin=0000
entered=""
entered=input("Enter a pin of your choice:")
while entered!=Right_pin:
    input("Enter the right pin:")
    break;
print(f"{Right_pin}is the correct pin,Access granted ")

    





    

