# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# ''' 

personName = str(input("Enter your name: "))

from datetime import datetime

date = datetime.now().strftime("%y,%m,%d")



letter = letter = '''
    Dear {name},
    You are selected!
    Date: {time}
 ''' 

filletered_letter = letter.format(name=personName,time= date)

print(filletered_letter)
 
 