"""
Developed by Orlando Companioni
Date: October 13 2022

Gets the average of inputed numbers
"""

#Allows the user to input values
def userInput():
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    return num1,num2   #return 2 values so it will need 2 variables

#calculates values

def calculation(val1,val2):
    total=(val1+val2)/2
    return total

#outputs the values
def output(val1,val2,total):
    print(f"The average of {val1} and {val2} is {total}")

#calls all the functions in one function
def main():
    num1, num2=userInput()  #provides a variable for each value
    average=calculation(num1,num2)
    output(num1,num2,average)
    
main()
    
    


