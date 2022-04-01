antenna = int(input('Enter number of antennas?: '))
eyes = int(input('\nEnter number of eyes?: '))

if ((antenna >=3) and (eyes <=4)):
    print('\nThe alien is TroyMartian') 
if ((antenna <=6) and (eyes >=2)):
    print('\nThe alien is VladSaturnian')
if ((antenna <=2) and (eyes <=3)): 
    print('\nThe alien is GrameMercurian')
