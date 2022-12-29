'''
Developed by Orlando Companioni
Date november 3 2022
calculates the factorial and the sum using recursion
'''
def main():
    user=int(input("enter a number"))
    num=factorial(user)
    sum=series(user)
    output(num,sum)

def factorial(num):
    if num<=1:
        return 1
    else:
        return num*factorial(num-1)

def series(num):
    if num<=0:
        return 0
    else: return num+series(num-1)   #adds num+num-1 until its = to 0 or less

def output(num,sum):
    print(f"the answer for factorial is {num} and the series is {sum}")
    

main()