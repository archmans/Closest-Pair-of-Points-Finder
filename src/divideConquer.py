import matplotlib.pyplot as plt
import random
import math
counterEuclidean = 0

def generate_points(n, m):
  #complexity O(n)
  points = []
  for i in range(n):
      temp = []
      for j in range(m):
          temp.append(random.randint(0,1000))
      points.append(temp)
  return points

def distance(p1,p2):
  #complexity O(1)
  global counterEuclidean
  counterEuclidean+=1
  result = float(0)
  for i in range(len(p1)):
      result += (p1[i]-p2[i])**2
  return math.sqrt(result)

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
    return s_strip(points)

def s_strip(points):
  #complexity O(nlogn)
  points.sort(key = lambda x: x[0])
  if(len(points) % 2 == 0):
    mid = int(len(points)/2)
  else:
    mid = int(len(points)//2) + 1
  left = points[:mid]
  right = points[mid:]
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
  for i in range(len(points)):
    if(abs(points[i][0] - points[mid][0]) < d):
      for j in range(i+1, len(points)):
        if(abs(points[j][0] - points[mid][0]) < d):
          if(distance(points[i], points[j]) < d):
            d = distance(points[i], points[j])
            p = points[i]
            q = points[j]
  return p, q, d  





