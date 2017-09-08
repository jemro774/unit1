#Jack Robey
#9/8/17
#slope.py - calculates the slope of a line given two points

x1 = float(input('Enter the x-value for your first coordinate: '))
y1 = float(input('Enter the y-value for your first coordinate: '))
x2 = float(input('Enter the x-value for your second coordinate: '))
y2 = float(input('Enter the y-value for your second coordinate: '))
slope = round((y2-y1)/(x2-x1), 2)
print('The slope is', slope)
b = round(-1*slope*x1+y1, 2)
print('The equation of the line is y =', slope, 'x +', b) 
