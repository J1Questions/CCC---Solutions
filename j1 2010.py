from sys import exit

n = int(input('Enter number: '))

if (1>n or 10<n):
    print('Number has to be less between or equal to 10 and 1')
    exit()
    
if ((n==1) or (n==9) or (n==10)):
    num = 1
    
elif ((n==2) or (n==3) or (n==7) or (n==8)):
    num = 2
    
elif ((n==4) or (n==5) or (n==6)):
    num = 3
    
print("There are",num,'possible combinations')


