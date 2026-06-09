#This is an age calculator
while True:
   print("\n........An amazing age calculator.......")
   try:
      currentdate=int(input("Enter the current year: "))
      print(f"The current date is: {currentdate}")
      Dateofbirth=int(input("Enter your date of birth: "))
      print("Your date of birth={Dateofbirth}")
      Age=currentdate-Dateofbirth
      print(Age)
      if Age<0:
        print("Error:year of birth cannot be greater  than current year.")
      else:
          print(f"Your date of birth is: {Dateofbirth}")
          print(f"The current year is:{currentdate}")
          print(f"Yes,your age is: {Age}")
   except ValueError:
     print("This is an error,enter the right age")
   again=input("\n do you want to calculate again,yes or no:").lower()
   if again != "yes":
      print("Thank you for using our age calculator")
      break
    

