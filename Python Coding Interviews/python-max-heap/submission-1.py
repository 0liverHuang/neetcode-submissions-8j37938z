import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
   new_reverse = [-num for num in nums]
   outcome = []
   heapq.heapify(new_reverse)
   while new_reverse:
        outcome.append(-heapq.heappop(new_reverse))
   return outcome




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
