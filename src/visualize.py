import matplotlib.pyplot as plt
import divideConquer as dc

def visualize_closest_pair3(points):
  #complexity O(nlogn)
  p, q, d = dc.closest_pair(points)
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

def visualize_closest_pair2(points):
  p, q, d = dc.closest_pair(points)
  x = []
  y = []
  for i in range(len(points)):
      if (points[i] != p and points[i] != q):
          x.append(points[i][0])
          y.append(points[i][1])
  fig = plt.figure()
  plt.scatter(x,y, c='b', )
  plt.scatter(p[0],p[1], color='r')
  plt.scatter(q[0],q[1], color='r')
  plt.plot([p[0],q[0]],[p[1],q[1]], color='r')
  plt.show()

def visualize_closest_pair1(points):
  p, q, d = dc.closest_pair(points)
  x = []
  for i in range(len(points)):
      if (points[i] != p and points[i] != q):
          x.append(points[i][0])
  fig = plt.figure()
  plt.scatter(x,[0]*len(x), c='b')
  plt.scatter(p[0],0, color='r')
  plt.scatter(q[0],0, color='r')
  plt.plot([p[0],q[0]],[0,0], color='r')
  plt.show()