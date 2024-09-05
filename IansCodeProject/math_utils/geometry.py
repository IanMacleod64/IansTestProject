import re
import pyinputplus as pyip
def area_of_circle():
    print('This funtion will find the area of a circle! ')
    print('What is the radius of the circle?')
    radius = input()
    if int(radius) > 0:
        radius = int(radius) * int(radius) * 3.14
        print('The area of your circle is:' + str(radius))
    else:
        print('That is not a radius. A radius must be a positive number.')

def area_of_a_rectangle():
    print('This function will find the area of a rectangle.')
    while True:
        print('What is the length of rectangle.')
        length = input()
        try:
            int(length) > 0
            break
        except:
            print('The length must be a positive number.')
    while True:
        print('What is the width of the rectangle')
        width = input()
        try:
            int(width) > 0
            rec_area = int(length) * int(width)
            print('The area of your rectangle is ' + str(rec_area))
            break
        except:
            print('The width must be a postive number.')
