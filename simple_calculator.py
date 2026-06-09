#Simple calculator
while True:
    print("\n............sarah's simple calculater......")
    try:
        number1=float(input("Enter your first number:"))
        operator=input("Enter an operator +,-,*,/,%,//:")
        number2=float(input("Enter the second number:"))
        if operator=="+":
            sum=number1+number2
            print(f"sum of the numbers= {sum}")
        elif operator=="-":
            difference=number1-number2
            print(f"The difference of the numbers= {difference}")
        elif operator=="*":
            product=number1*number2
            print(f"The product of the numbers = {product}")
        elif operator=="/":
            if number2==0:
                print("Error:you cannot divide by zero")
            else:
                quotient=number1/number2
                print(f"The quotient of the numbers= {quotient}")
        elif operator=="%":
            if number2==0:
                print("Error:You cannot divide by zero")
            else:
                remainder=number1%number2
                print(f"The remainder ={remainder}")
        else:
            print("Error:invalid operator,please use +,-,*,/,%,//")
    except ValueError:
        print("Error:please print numbers only.")

    again=input("\n Do you want to perform another calculation?yes/no:").lower()
    if again !="yes":
        print("Thank you for using the calculater.Goodbye")
        break