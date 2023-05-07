import string as str 
import random as ran

user = (int(input("Enter Password Length: ")))
print('''Choose Character Set From These:
        1. Digits
        2. Letters
        3. Symbols 
        4. Exit ''')
charlist = ''
count = 0
while count <=2:
    choice = int(input('Pick a number: '))
    if (choice == 1):
        charlist += str.ascii_letters 
    elif (choice == 2):
        charlist +=  str.digits 
    elif (choice == 3):
        charlist += str.punctuation
    else:
        print('Please pick a valid option! ')
    count=count+1
        
if not charlist:
    print('No character will be Selected. Existing...')
    exit()
password = []
for i in range(user):
    randomchar = ran.choice(charlist)
    password.append(randomchar)
print('Your generated password is: ',"".join(password))
