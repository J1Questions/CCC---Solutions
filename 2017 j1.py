x = int(input('Enter x: '))
y = int(input('Enter y: '))
if -1000<=x<=1000 and x != 0:
    x1 = x
if -1000<=y<=1000 and y != 0:
    y1 = y
if x<=-1 and y<=-1:
    print("The point is in Quadrant 3")
elif x>=1 and y<=-1:
    print('The point is in Quadrant 4')
elif x>=1 and y>=1:
    print('The point is in Quadrant 1')
elif x<=-1 and y>=1:
    print('The point is in Quadrant 2')


