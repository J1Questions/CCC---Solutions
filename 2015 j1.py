month=int(input("Enter the month:"))
day=int(input("Enter the day: "))
if((month<2) and (day<18)):
  print("Before")
elif((month>2) and (day>18)):
  print("After")
elif((month==2) and (day==18)):
  print("Special")

