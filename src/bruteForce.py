import divideConquer as dc

def closest_pair_bf(points):
  #complexity O(n^2)
  # brute force
  d = dc.distance(points[0], points[1])
  p = points[0]
  q = points[1]
  for i in range(len(points)):
    for j in range(i+1, len(points)):
      if(dc.distance(points[i], points[j]) < d):
        d = dc.distance(points[i], points[j])
        p = points[i]
        q = points[j]
  return p, q, d