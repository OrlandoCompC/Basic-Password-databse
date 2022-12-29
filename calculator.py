"""
developed by Orlando Companioni
Date: October 18 2022

Create a calculator which calculates the answers and outputs them but in a function

"""
#Main function which calls other functions
def main():
    number1,number2=user_input()
    sum,sub,multiply,division=calculation(number1,number2)
    answer(sum,sub,multiply,division)

#gets the input from the user
def user_input():
    num1=int(input("Please enter a number: "))
    num2=int(input("Please enter a 2nd number: "))
    return num1,num2

#does the calculations
def calculation(num1,num2):  #gets the two numbers and does all the calcs
    sum=num1+num2
    sub=num1-num2
    multiply=num1*num2
    divide=num1/num2
    return sum,sub,multiply,divide  # returns the values I want to later print

#outputs the answer
def answer(sum,sub,multiply,divide):     #putting the variables I want to print
    print(f"The sum is {sum}\nThe substraction is {sub}\
\nThe multiplication is {multiply}\nThe divisionis {divide}")
    
main()
    

    
    
