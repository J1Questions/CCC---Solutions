Burger = int(input('Enter your choise of burger: ')) # This assigns variables to your input on the type of burger you want.
Side = int(input('\nEnter your choise of side: '))
Drink = int(input('\nEnter your choise of drink: '))
Dessert = int(input('\nEnter your choise of dessert: '))
total1 = 0 
if Burger == 1: # This if statement checks if the type of burger matches with the cheeseburger option.
  total1 = total1 + 461 # This line adds the previous total calories with your new choise of burger.
elif Burger == 2: # The format used in the last two lines is repeated 4 times for each food choise to check for every item on the menu.
  total1 = total1 + 431
elif Burger == 3:
  total1 = total1 + 420
elif Burger == 4:
  total1 = total1
if Side == 1:
  total1 = total1 + 100
elif Side == 2:
  total1 = total1 + 57
elif Side == 3:
  total1 = total1 + 70
elif Side == 4:
  total1 = total1
if Drink == 1:
  total1 = total1 + 130
elif Drink == 2:
  total1 = total1 + 160
elif Drink == 3:
  total1 = total1 + 118
elif Drink == 4:
  total1 = total1
if Dessert == 1:
  total1 = total1 + 167
elif Dessert == 2:
  total1 = total1 + 266
elif Dessert == 3:
  total1 = total1 + 75
elif Dessert == 4:
  total1 = total1 
print("\nYour Total Calorie Count Is:",total1) # This line outputs your total calorie count of all of the foods you chose.
