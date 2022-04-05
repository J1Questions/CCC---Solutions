antenna = int(input('Enter number of antennas?: '))
eyes = int(input('\nEnter number of eyes?: '))

check = False
if ((antenna >=3) and (eyes <=4)):
    print('\nThe alien is TroyMartian')
    check = True
if ((antenna <=6) and (eyes >=2)):
    print('\nThe alien is VladSaturnian')
    check = True
if ((antenna <=2) and (eyes <=3)): 
    print('\nThe alien is GrameMercurian')
    check = True
if (check==False):
    print('Alien not identified')
