import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for index, point in enumerate(points):
            distance = (point[0]**2 + point[1]**2) ** 0.5
            heapq.heappush(heap, (distance, index))
        
        res = []
        for i in range(k):
            _, index = heapq.heappop(heap)
            res.append(points[index])
        
        return res