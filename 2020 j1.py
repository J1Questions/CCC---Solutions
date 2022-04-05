#Inputs
small_treats = int(input())
medium_treats = int(input())
large_treats = int(input())

#Computation
hapiness_score = 1*small_treats + 2*medium_treats + 3*large_treats

#Outputs
if (hapiness_score>=10):
    print("happy")

else:
    print("sad")


