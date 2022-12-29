"""
Developed by Orlando Companioni
Date: oct 6 2022

user inputs date we output it
"""
date=(input("what is the date dd/mm/yyyy: "))
#make it into a list
list=date.split("/")

#assign each value of the list to a variable
day=list[0]
month=list[1]
year=list[2]
output1=""
output2=""
output3=""

#output the list with its restrictions
if int(day)>0 and int(day)<31:
   output1=f"The day is {list[0]}"
   if int(month)>0 and int(month)<=12:
      output2=f"The month is {list[1]}"
      if int(year)>1900 and int(year)<3000:
          output3=(f"The year is {list[2]}")
          print(output1)
          print(output2)
          print(output3)
      else:print("Invalid date")
   else:print("Invalid date")
else:print("Invalid date")
    



