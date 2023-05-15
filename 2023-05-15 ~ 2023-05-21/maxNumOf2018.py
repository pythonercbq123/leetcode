from typing import List


def nums_of_sum2018(a: List[int]) -> int:
    sorted_a = sorted(a)
    # 使用双指针
    left = 0
    right = len(a) - 1
    count = 0
    while left < right:
        left_val = sorted_a[left]
        right_val = sorted_a[right]
        if left_val + right_val == 2018:
            count += 1
            left += 1
            right -= 1
            while left < right and sorted_a[left] == left_val:
                left += 1
            while left < right and sorted_a[right] == right_val:
                right -= 1
        elif left_val + right_val < 2018:
            left += 1
        else:
            right -= 1
    return count


def min_cost(n, m):
    cost = [float('inf')] * (n + 1)
    cost[1] = 0

    for i in range(1, n + 1):
        for j in range(0, i):
            if i - j <= m:
                cost[i] = min(cost[i], cost[j] + j * (i - j))

    return cost[2], cost[n]


if __name__ == '__main__':
    res = nums_of_sum2018([1, 500, 1518, 500, 2017])
    print(res)
    res = min_cost(5, 2)
    print(res)