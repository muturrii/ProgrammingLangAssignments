# Anthony Muturi Karugu SCT211-0016/2022
#To be a leap year, the year number must be divisible by four except for end of century years
# which must be divisible by 400

import math
while True:
    try:
        year = int(input('Enter year: '))
        break
    except:
        print('Invalid! Please try again.')
        continue
temp = math.ceil(year/100) * 100

if temp == year:
    if (year % 400) != 0:
        print(year, 'is not a leap year')
    else:
        print(year, 'is a leap year!')
else:
    if (year % 4) != 0:
        print(year, 'is not a leap year')
    else:
        print(year, 'is a leap year!')
