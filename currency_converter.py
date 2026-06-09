#My currency converter
while True:
    print("\n.... Currency Converter....")
    #Declaire all variables
    print("\Buying prices")
    Buying_USD= float(3600)
    Buying_EURO=float(4500)
    Buying_POUND=float(5000)
    Selling_USD=float(3700)
    Selling_EURO=float(5000)
    Selling_POUND=float(5500)
    try:
       Action=input("What would you like to do,sell or buy?:").lower()
       currency=input("What currency do you have? USD,EURO,OR POUND:").upper()
       Currency_Amount=float(input("How much is it:"))
       if Action=="buy":
          if currency=="USD":
            TotalUGX_Dollar=Buying_USD*Currency_Amount
            print(f"The total amount you will get is: {TotalUGX_Dollar}")
          elif currency=="EURO":
            TotalUGX_Euro=Buying_EURO*Currency_Amount
            print(f"The total amount you will get is:{TotalUGX_Euro}")
          elif currency=="POUND":
            TotalUGX_Pound=Buying_POUND*Currency_Amount
            print(f"The total amount you will get is: {TotalUGX_Pound}")
          else:
            print("Error:Invalid currency.please Enter USD,EURO,or POUND.")
       elif Action=="sell":
        if currency=="USD":
            TotalUGX_Dollar2=Selling_USD*Currency_Amount
            print(f"The Total Amount is:{TotalUGX_Dollar2}")
        elif currency=="EURO":
            TotalUGX_Euro2=Selling_EURO*Currency_Amount
            print(f"The total amount is:{TotalUGX_Euro2} ")
        elif currency=="POUND":
            TotalUGX_Pound2=Selling_POUND*Currency_Amount
            print(f"You will pay UGX {TotalUGX_Pound2}")
        else:
            print("Error:Invalid currency.please enter USD,EURO,or POUND.")
    except ValueError:
     print(input("You entered The wrong value,would you please enter the right value:"))
    again=input("Would you like to do something else?yes/no:").lower()
    if again!="yes":
       print("Thank you for using this converter")
       break
     

        
        



    