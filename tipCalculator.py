#Jack Robey
#9/8/17
#tipCalculator.py - calculates the tip amount

mealPrice = float(input('What is the price of your meal? '))
tipPercentage = int(input('What is the percentage you wish to tip? '))
mealTip = round(mealPrice*(tipPercentage/100), 2)
print('You should tip', mealTip, 'dollars')

