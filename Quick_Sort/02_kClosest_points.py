import heapq

def kClosest(points, k):
    # Method 1: Easy Sorting (O(N log N))
    # Distance score (x^2 + y^2) ke basis par sort karke pehle k points le lo
    return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]
