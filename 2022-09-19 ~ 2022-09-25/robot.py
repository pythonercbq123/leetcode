from typing import List


class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        mx = 0
        my = 0
        n = len(command)
        for i in range(n):
            if command[i] == 'U':
                my += 1
            else:
                mx += 1
        if self.can_reach(mx, my, command, x, y):
            return False
        for ob in obstacles:
            dest_x, dest_y = ob
            if dest_x <= x and dest_y <= y and not self.can_reach(mx, my, command, dest_x, dest_y):
                return False
        return True

    def can_reach(self, mx, my, command, dest_x, dest_y):
        loops = min(dest_x // mx, dest_y // my)
        dest_x = dest_x - loops * mx
        dest_y = dest_y - loops * my
        for c in command:
            if dest_y == 0 and dest_x == 0:
                return False
            if c == 'U':
                dest_y -= 1
            else:
                dest_x -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    ret = s.robot("URR", [[4, 2]], 3, 2)
    print(ret)
