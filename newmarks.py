"""
Developed by : Orlando Companioni
date: sep 27 2022
Get the users marks and then output them
"""
finalMark=" "
again="y"


#Get input from the user
while again=="y":     
  mark=int(input("what is your mark: "))

  #Compare input with our conditions

  if mark>=0 and mark<=100:
    if mark>=90:
      finalMark=f"your mark is an A+"
    elif mark>=80:
      finalMark=f"your mark is an A"
    elif mark>=70:
      finalMark=f"your mark is an B"
    elif mark>=60:
      finalMark=f"your mark is an C"
    else: finalMark=f"your mark is an F"
  else:print("invalid answer")

  #Output the final mark
  print(finalMark)
  again=input("try again?(y/n)")


