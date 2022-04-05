weight_1 = int(input(" "))
weight_2 = int(input(" "))
weight_3 = int(input(" "))

if (weight_3 < weight_1 < weight_2 or weight_2 < weight_1 < weight_3):
    print(weight_1)

elif (weight_3 < weight_2 < weight_1 or weight_1 < weight_2 < weight_3):
    print(weight_2)

elif (weight_1 < weight_3 < weight_2 or weight_2 < weight_3 < weight_1):
    print(weight_3)


