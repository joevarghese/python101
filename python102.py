day = int(input('Day (0-6)? '))

if day == 0:
    print("Today is Sunday")

elif day == 1:
    print("Today is Monday")

elif day == 2:
    print("Today is Tuesday")    

elif day == 3:
    print("Today is Wednesday") 

elif day == 4:
    print("Today is Thursday") 

elif day == 5:
    print("Today is Friday") 

elif day == 6:
    print("Today is Saturday")    

celcius = int(input("What is the temperature in Celcius? "))

farenheit = (celcius * 1.8) + 32
print(f"The current temperature is {farenheit}F")

while True:
    try:
        bill = int(input("What is your bill amount? "))
        print(f"The number you entered {bill} ")

        service = input("How was your service: Good, Fair, or Bad? ")

        service = service.lower()

        if service == "good":
            tip = bill * .20
            totalbill = tip + bill
            print(f"Your tip amount is {tip} ")
            print(f"Your total bill amount is {totalbill} " )
            break
        elif service == "fair":
            tip = bill * .15
            totalbill = tip + bill
            print(f"Your tip amount is {tip} ")
            print(f"Your total bill amount is {totalbill} " ) 
            break
        elif service == "bad":
            tip =  bill * .10
            totalbill = tip + bill
            print(f"Your tip amount is {tip} ")
            print(f"Your total bill amount is {totalbill} " )
            break

    except ValueError:
        print("please try again")


test = int(input("What number would you like to begin"))
test3 = int(input("What number would you like to end "))

while test <= test3:


        print(test)
        test = test + 1

counter = int(input("select a number of stars to print")) 
while 1 <= counter:
    print("*****")
    counter = counter + 1
