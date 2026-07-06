from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1

        heap = []
        for n, count in frequency.items():
            heapq.heappush(heap, (count, n))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for count, n in heap:
            result.append(n)

        return result
