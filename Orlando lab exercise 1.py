"""Lab 1
Set-B
Course: PROG12974
Name:Orlando Companioni
Submission date: oct 11 2022
Date created: oct 11 2022
Exercise 1

Takes words as input then outputs a sentence and counts the amount of words
"""

word=""
length=""
letterCounter=0
twoletterCounter=0      #counters and variables
threeletterCounter=0
fourletterCounter=1
fiveletterCounter=0
totalCount=2
sentence="""Orlando says,\""""


while word !=".":      #checks the conditions to add the counters and form the sentence
    word=input(" Enter a word(Enter a '.' to terminate):")
    length=len(word)
    if length==1 and word !=".":  #counts the word depending on how many letters
        letterCounter+=1          #not counting the .
      
    elif length==2 and word !=".":
        twoletterCounter+=1
        
    elif length==3 and word !=".":
        threeletterCounter+=1
        
    elif length==4 and word !=".":
        fourletterCounter+=1
        
    elif length==5 and word !=".":
        fiveletterCounter+=1
       
    if word !=".":
        totalCount+=1
    
    
    if word !=".":
        sentence+=" "+word       #separates the words except for the .
    else: sentence+=word
    

    #outputs the values
print(f"""{sentence}\"""")
print(f"Total word count:{totalCount}")
print(f"One letter word count:{letterCounter}")
print(f"Two letter word count:{twoletterCounter}")
print(f"Three letter word count:{threeletterCounter}")
print(f"Four letter word count:{fourletterCounter}")
print(f"five letter word count:{fiveletterCounter}")

    

