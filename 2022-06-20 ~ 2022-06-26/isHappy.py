class Solution:

    def is_happy(self, n: int) -> bool:
        memo = set()
        while n != 1 and n not in memo:
            memo.add(n)
            self.get_next(n)
        return n == 1

    def get_next(self, n: int) -> int:
        total = 0
        while n > 0:
            n, mod = divmod(n, 10)
            total += mod ** 2
        return total

    def slow_fast(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)
        while fast != 1 and slow != fast:
            slow = self.get_next(n)
            fast = self.get_next(self.get_next(fast))
        return fast == 1