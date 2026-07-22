import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        heapq.heapify(self.heap)

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

KthLargestObj = KthLargest(3, [4, 5, 8, 2])
print(KthLargestObj.add(3))  # returns 4
print(KthLargestObj.add(5))  # returns 5
print(KthLargestObj.add(10))  # returns 5