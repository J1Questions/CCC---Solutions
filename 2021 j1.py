temperature = int(input("Enter temperature"))

atm_pressure = 5 * temperature - 400

if (atm_pressure == 100):
    sea_level = 0

elif (atm_pressure <100):
    sea_level = 1

elif (atm_pressure <100):
    sea_level = -1

print(atm_pressure)
print(sea_level)
