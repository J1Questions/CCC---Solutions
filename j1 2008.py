import math
h = float(input('enter height in Meters: '))
w = float(input('enter height in KG: '))

bmi = w/(h**2)
rbmi = round(bmi,1)

if (rbmi > 25):
    message = ('overweight')
    
elif (18.5<= rbmi <= 25):
    message = ('Normal')
    
else:
    message = ('underweight')

print(message)
