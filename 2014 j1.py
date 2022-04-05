a1=int(input('angle 1: '))
a2=int(input('angle 2: '))
a3=int(input('angle 3: '))

check = a1+a2+a3

if ((check != 180) or (a1 == 0) or (a2 == 0) or (a3 == 0)):
    total = ('error')
    
elif ((a1==60) and (a2==60) and (a3==60)):
    total = ("Equilateral")
    
elif ((check == 180) and (a1 == a2) or (a2 == a3) or (a1 == a3)):
    total = ('isosolese')
    
elif ((check == 180) and (a1 != a2) or (a2 != a3) or (a1 != a3)):
    total = ('scalene')
    
print(total)
    
