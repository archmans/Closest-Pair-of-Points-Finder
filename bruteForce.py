import numpy as np 
import matplotlib.pyplot as plt
import random
import math

#Find closest pair of points in a set of x,y,z coordinates
#Generate random points based on n input and insert to list
def generate_points(n, m):
  #complexity O(n)
    points = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(random.randint(0,1000))
        points.append(temp)
    return points


n = int(input("Enter number of points: "))
points = generate_points(n)
print(points)

# #visualize points with matplotlib
# def visualize(points):
#     x = []
#     y = []
#     z = []
#     for i in range(len(points)):
#         x.append(points[i][0])
#         y.append(points[i][1])
#         z.append(points[i][2])
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.scatter(x,y,z)
#     plt.show()

# visualize(points)

#Find distance between two points
def distance(p1,p2):
  #complexity O(1)
    global counterEuclidean
    counterEuclidean+=1
    result = float(0)
    for i in range(len(p1)):
        result += (p1[i]-p2[i])**2
    return math.sqrt(result)
#Find closest pair of points

#color the closest pair of points and draw the line between them
def visualize_closest_pair(points):
    min_distance = distance(points[0],points[1])
    p1 = points[0]
    p2 = points[1]
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            if distance(points[i],points[j]) < min_distance:
                min_distance = distance(points[i],points[j])
                p1 = points[i]
                p2 = points[j]
    x = []
    y = []
    z = []
    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])
        z.append(points[i][2])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,y,z)
    ax.scatter(p1[0],p1[1],p1[2],color='red')
    ax.scatter(p2[0],p2[1],p2[2],color='red')
    ax.plot([p1[0],p2[0]],[p1[1],p2[1]],[p1[2],p2[2]],color='red')
    plt.show()

#print all distances between points sorted in ascending order
def print_distances(points):
    distances = []
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            distances.append(distance(points[i],points[j]))
    distances.sort()
    print(distances)

print_distances(points)
visualize_closest_pair(points)