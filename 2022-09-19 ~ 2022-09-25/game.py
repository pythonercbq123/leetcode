from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        n = len(guess)
        count = 0
        for i in range(n):
            if guess[i] == answer[i]:
                count += 1
        return count