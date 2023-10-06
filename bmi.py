# Anthony Muturi Karugu SCT211-0016/2022

weight = float(input('Enter your weight in kilograms: '))
height = float(input('Enter your height in meters: '))

bmi = weight / (height * height)

if bmi <= 18.4:
    print('Your Body Mass Index - BMI is', round(bmi, 2), '.You are underweight.')
elif bmi <= 24.9:
    print('Your Body Mass Index - BMI is', round(bmi, 2), '.You have normal weight.')
elif bmi <= 39.9:
    print('Your Body Mass Index - BMI is', round(bmi, 2), '.You are overweight.')
else:
    print('Your Body Mass Index - BMI is', round(bmi, 2), '.You are obese.')