import math
 
weight = float(input())
height = float(input())
bmi = weight/(height * height)
roundedbmi = (bmi,1)
 
if roundedbmi > 25.0:
   print("Overweight")
elif 18.5 <= roundedbmi <= 25.0:
   print("Normal weight")
elif roundedbmi < 18.5:
   print("Underweight")
