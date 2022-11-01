from collections import deque


class MovingAverage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.nums = deque()
        self.sum = 0

    def next_average(self, val):
        self.nums.append(val)
        self.sum += val
        if len(self.nums) > self.capacity:
            pop_val = self.nums.popleft()
            self.sum -= pop_val
        return self.sum / len(self.nums)


if __name__ == '__main__':
    s = MovingAverage(3)
    for num in [1, 2, 3, 4, 5, 6]:
        ret = s.next_average(num)
        print(ret)
