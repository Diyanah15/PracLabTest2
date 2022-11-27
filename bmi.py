def calculate_bmi(height, weight):
    bmi = weight/(height**2)

    if (bmi < 18.5):
        return -1

    elif (bmi >= 18.5 and bmi <=25.0):
        return 0

    elif (bmi > 25.0):
        return 1

height = float(input('Enter Height: '))
weight = float(input('Enter Weight: '))
value = calculate_bmi(height, weight)
print('You are ' +str(value))