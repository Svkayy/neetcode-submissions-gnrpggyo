import heapq

class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        self.q = []
        self.k = k
        for num in nums:
            heapq.heappush(self.q, -num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.q, -val)

        tmp = []
        curr = self.k
        while curr > 0:
            tmp.append(heapq.heappop(self.q))
            curr -=1

        res = -tmp[-1]

        for num in tmp:
            heapq.heappush(self.q, num)

        return res

