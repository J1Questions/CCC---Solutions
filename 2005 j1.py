#j1 2005
daytime=float(input("Number of daytime minutes?"))
evening=float(input("Number of evening  minutes?"))
weekend=float(input("Number of weekend  minutes?"))
if(daytime>=100):
   daytime_a=daytime-100
elif(daytime<100):
   daytime_a=0
if(daytime>=250):
   daytime_b=daytime-250
elif(daytime<250):
   daytime_b=0
planA=round((daytime_a*0.25+evening*0.15+weekend*0.20),2)
planB=round((daytime_b*0.45+evening*0.35+weekend*0.25),2)
print("Plan A costs " , planA)
print("Plan B costs", planB)
if(planA>planB):
  print("Plan B is cheapest")
elif(planA==planB):
  print("Plan A and B are same price")
elif(planA<planB):
  print("Plan A is cheapest")

