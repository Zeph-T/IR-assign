import numpy as np
import math
from operator import add

print("Enter the coordinates of the point: ")
point=list(map(int,input().split()))

axes = ['x','y','z']
print(point)
for i in axes:
    new_points = []
    print("Rotation w.r.t " + i + " Axis(in degrees)(negative value for CW):")
    degrees = math.radians(int(input()))
    if i=='x':
    	new_points=[point[0], point[1]*math.cos(degrees) - point[2]*math.sin(degrees), point[1]*math.sin(degrees) + point[2]*math.cos(degrees)]
    if i=='y':
    	new_points=[ point[0]*math.cos(degrees) - point[2]*math.sin(degrees)  ,  point[1] ,  point[0]*math.sin(degrees) + point[2]*math.cos(degrees)  ]
    if i=='z':
    	new_points=[point[0]*math.cos(degrees) - point[1]*math.sin(degrees)  ,  point[0]*math.sin(degrees) + point[1]*math.cos(degrees)  , point[2] ]

    point = new_points

print("New point after rotations :")
print(point)
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print("Enter the translations w.r.t x,y,z:")
trans = [int(input()) for i in range(3)]
final = list(map(add, point, trans)) 
print(final)
