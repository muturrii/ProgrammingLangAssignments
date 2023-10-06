# Anthony Muturi Karugu SCT211-0016/2022

import math
totalAmount,numberOfPeople = None,None

while True:
    try:
        totalAmount = int(input('What is the total bill? '))
        break
    except:
        print('Please enter a number!')
        continue

while True:    
    try:
        numberOfPeople = int(input('How many people are splitting the bill? '))
        break
    except:
        print('Please enter a number!')
        continue

while True:
    print('Enter the bill percent choice; \n A.10%        B.12%         C.15%')
    tipChar = input().capitalize()

    amountPP = None
    match tipChar:
        case 'A':
            amountPP = (0.1 * totalAmount + totalAmount) / numberOfPeople
            print('The payable amount is', "%.2f" % amountPP, 'per person.')
            quit()
        case 'B':
            amountPP = (0.12 * totalAmount + totalAmount) / numberOfPeople
            print('The payable amount is', "%.2f" % amountPP, 'per person.')            
            quit()
        case 'C':
            amountPP = (0.15 * totalAmount + totalAmount) / numberOfPeople
            print('The payable amount is', "%.2f" % amountPP, 'per person.')
            quit()
        case other:
            print('Invalid Choice! Please try again.')
