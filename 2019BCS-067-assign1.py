import numpy as np
import math
from operator import add

print("Enter the coordinates of the point: ")
a=int(input())
b=int(input())
c=int(input())
point = [a,b,c]

axes = ['x','y','z']
print(point)
for i in axes:
    new_points = []
    print("Rotation w.r.t " + i + "-axis(in degrees)(enter neg value for CW):")
    degrees = math.radians(int(input()))
    if i=='x':
        new_points.append(point[0])
        new_points.append((point[1]*math.cos(degrees)) - point[2]*math.sin(degrees))
        new_points.append((point[1]*math.sin(degrees)) + point[2]*math.cos(degrees))
    if i=='y':
        new_points.append((point[0]*math.cos(degrees)) - point[2]*math.sin(degrees))
        new_points.append(point[1])
        new_points.append((point[0]*math.sin(degrees)) + point[2]*math.cos(degrees))
    if i=='z':
        new_points.append((point[0]*math.cos(degrees)) - point[1]*math.sin(degrees))
        new_points.append((point[0]*math.sin(degrees)) + point[1]*math.cos(degrees))
        new_points.append(point[2])

    point = new_points

print("new points after rotations = ")
print(point)

print("Enter the translations w.r.t x,y,z respectively: ")
trans = [int(input()) for i in range(3)]
final = list(map(add, point, trans)) 
print(final)