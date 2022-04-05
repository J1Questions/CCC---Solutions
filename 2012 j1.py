speed_limit = int(input("what is the speed limit: "))
user_speed = int(input("What speed were you going at: "))

speed_math = user_speed - speed_limit

if (user_speed <= speed_limit):
    response = "Congratulations, you are within the speed limit!"

elif (1 <= speed_math <= 20):
    response = "Fine $100"

elif (21 <= speed_math <= 30):
    response = "Fine $270"

elif (speed_math >= 31):
    response = "Fine $500"

print(response)

