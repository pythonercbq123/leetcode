from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        import heapq
        heap = []
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        for key, val in hashmap.items():
            if len(heap) >= k:
                if val > heap[0][0]:
                    heapq.heapreplace(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        return [item[1] for item in heap]


if __name__ == '__main__':
    s = Solution()
    ret = s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(ret)