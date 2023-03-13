from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        consumed_energy = sum(energy)
        if consumed_energy - initialEnergy < 0:
            training_hours = 0
        else:
            training_hours = consumed_energy - initialEnergy + 1

        for i in experience:
            if i >= initialExperience:
                training_hours += (i - initialExperience) + 1
                initialExperience = 2 * i + 1
            else:
                initialExperience += i

        return training_hours


if __name__ == '__main__':
    s = Solution()
    ret = s.minNumberOfHours(5, 3, [1, 4, 3, 2], [2, 6, 3, 1])
    print(ret)
    ret = s.minNumberOfHours(2, 4, [1], [3])
    print(ret)

