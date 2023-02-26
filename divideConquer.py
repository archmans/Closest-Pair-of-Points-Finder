import numpy as np 
import matplotlib.pyplot as plt
import random
import math
import platform
import time
import os
counterEuclidean = 0

def generate_points(n):
  #complexity O(n)
    points = []
    for i in range(n):
        x = random.randint(0,100)
        y = random.randint(0,100)
        z = random.randint(0,100)
        points.append([x,y,z])
    return points

def distance(p1,p2):
  #complexity O(1)
    global counterEuclidean
    counterEuclidean+=1
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def closest_pair(points):
  #complexity O(nlogn)
  if(len(points) == 2):
    return points[0], points[1], distance(points[0], points[1])
  elif(len(points) == 3):
    d1 = distance(points[0], points[1])
    d2 = distance(points[0], points[2])
    d3 = distance(points[1], points[2])
    if(d1 < d2 and d1 < d3):
      return points[0], points[1], d1
    elif(d2 < d1 and d2 < d3):
      return points[0], points[2], d2
    else:
      return points[1], points[2], d3
  else:
    return last_step(points)

def last_step(points):
  #complexity O(nlogn)
  points.sort(key = lambda x: x[0])
  if(len(points) % 2 == 0):
    mid = int(len(points)/2)
  else:
    mid = int(len(points)//2) + 1
  left = points[:mid]
  right = points[mid:]
  # print("left", left)
  # print("right", right)
  p1, q1, d1 = closest_pair(left)
  p2, q2, d2 = closest_pair(right)
  if(d1 < d2):
    d = d1
    p = p1
    q = q1
  else:
    d = d2
    p = p2
    q = q2
  midx = points[mid][0]
  midy = points[mid][1]
  midz = points[mid][2]
  new_list = []
  for i in range(len(points)):
    if(abs(points[i][0] - midx) < d or abs(points[i][1] - midy) < d or abs(points[i][2] - midz) < d):
      new_list.append(points[i])
  for i in range(len(new_list)):
    for j in range(i+1, len(new_list)):
      if(distance(new_list[i], new_list[j]) < d):
        d = distance(new_list[i], new_list[j])
        p = new_list[i]
        q = new_list[j]
  return p, q, d  

def visualize_closest_pair(points):
  #complexity O(nlogn)
    p, q, d = closest_pair(points)
    x = []
    y = []
    z = []
    for i in range(len(points)):
      if(points[i] != p and points[i] != q):
        x.append(points[i][0])
        y.append(points[i][1])
        z.append(points[i][2])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,y,z)
    ax.scatter(p[0],p[1],p[2], color='r')
    ax.scatter(q[0],q[1],q[2], color='r')
    ax.plot([p[0],q[0]],[p[1],q[1]],[p[2],q[2]], color='r')
    plt.show()

def visualize_closest_pair_bf(points):
  #complexity O(n^2)
    p1, q1, d1 = closest_pair_bf(points)
    last_step(points, p1, q1, d1)
    x = []
    y = []
    z = []
    for i in range(len(points)):
      if(points[i] != p and points[i] != q):
        x.append(points[i][0])
        y.append(points[i][1])
        z.append(points[i][2])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,y,z).set_color('blue')
    ax.scatter(p[0],p[1],p[2]).set_color('red')
    ax.scatter(q[0],q[1],q[2]).set_color('red')
    ax.plot([p[0],q[0]],[p[1],q[1]],[p[2],q[2]]).set_color('red')  
    plt.show()

def closest_pair_bf(points):
  #complexity O(n^2)
  # brute force
  d = distance(points[0], points[1])
  p = points[0]
  q = points[1]
  for i in range(len(points)):
    for j in range(i+1, len(points)):
      if(distance(points[i], points[j]) < d):
        d = distance(points[i], points[j])
        p = points[i]
        q = points[j]
  return p, q, d

n = int(input("Masukkan jumlah titik: "))
while(n < 2):
    n = int(input("Masukkan jumlah titik: "))

points = generate_points(n)    
os.system('cls' if os.name == 'nt' else 'clear')
print("============================================================")
print("                 Divide & Conquer Algorithm                 ")
print("============================================================")
startTime1 = time.time()
p, q, d = closest_pair(points)
endTime1 = time.time()
totalTime1 = (endTime1 - startTime1)*1000
print("Waktu eksekusi divide and conquer: ", totalTime1, "ms")
print("Jumlah operasi euclidean: ", counterEuclidean)
print("Jarak terdekat: ", d)
print("Platform: ", platform.processor())
print("===========================================================")
print("                   Brute Force Algorithm                   ")
print("===========================================================")

startTime2 = time.time()
p1, q1, d1 = closest_pair_bf(points)
endTime2 = time.time()
totalTime2 = (endTime2 - startTime2)*1000
print("Waktu eksekusi brute force: ", totalTime2, "ms")
print("Jumlah operasi euclidean brute force: ", counterEuclidean)
print("Platfprm: ", platform.processor())
print("Jarak terdekat: ", d1)
print("============================================================")
print("Apakah anda yakin ingin melihat visualisasi? (yay/nay)")
answer = input()
if(answer == 'yay'):
  visualize_closest_pair(points)
else:
  print("Thank you for using our program!")