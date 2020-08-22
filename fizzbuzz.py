#Get user number input
number = int(input("Select a number to count "))
#print out all numbers from 1 to that number

for test in range(1,number + 1):
    if test % 3 == 0 and test % 5 == 0:
        print("fizzbuzz")
    elif test % 3 == 0:
        print("fizz")
    elif test % 5 == 0:
        print("buzz")
    
    else:
        print(test)

#for every number divisible by 3 print out fizz

#for every number divisible by 5 print out buzz

#for every number divisible by 3 and 5 print out fizzbuzz

