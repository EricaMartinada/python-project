# filename  : Martinada_e4.py
#author     : Erica Martinada
# description :  this is a python program
#                that compute and displays
#                the triangle's perimeter 
#                and area
#               


def triangle_perimeter(a, b, c):
#Prompt for input
line = input ("Enter the side lengths of a triangle: ")
#line = '3,4,5'

(a,b,c) = (float (x) for x in line.split (","))

P = triangle_perimeter (a,b,c)
A = triangle_heronsarea (a,b,c)



def triangle_heronsarea (a,b,c):
    s = triangle_perimeter(a,b,c) / 2


    area = sqrt (s* (s-a) * (s-b) * (s-c))
    return area

 print 