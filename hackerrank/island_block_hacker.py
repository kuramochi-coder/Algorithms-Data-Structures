import fileinput
import math

arr = []
poly_points = []
n = []
m = []
ab_points = []

def readInput():
    for line in fileinput.input():
        arr.append(line.rstrip())
    
    n.append(int(arr[0].split(sep=" ")[0]))
    m.append(int(arr[1+n[0]].split(sep=" ")[0]))
    for i in range(1, 1+n[0]):
        poly_points.append(arr[i].split(sep=" "))
        
    for j in range(2+n[0], len(arr)):
        ab_points.append(arr[j].split(sep=" "))

def calcDistance(a):
    for i in range(len(a)):
        p = a[i]
        x_dist = p[2] - p[0]
        y_dist = p[3] - p[1]
        
        return math.sqrt(x_dist*x_dist + y_dist*y_dist)
    

def findClosestPoints(points):
    shortest_dist = float('inf')
    p = []
    for point in points:
        
        current_dist = 0
        x1 = int(point[0])
        y1 = int(point[1])
        
        x2 = int(point[2])
        y2 = int(point[3])
        
        p.append([x1, y1, x2, y2])
    
        current_dist += calcDistance(p)
        shortest_dist = min(shortest_dist, current_dist)
    
    print(shortest_dist)
    
    

def convex_hull(points):
    """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """

    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(set(points))

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    return lower[:-1] + upper[:-1]

readInput()
# print(arr)
# print(n)
# print(m)
# print(poly_points)
# print(ab_points)
findClosestPoints(ab_points)
