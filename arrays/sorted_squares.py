from typing import List

class Solution():
    def square(self, a: int) -> int:
        return a * a

    def squares_sorted_array(self, a : List[int]) -> List[int]:
        b = []
        if len(a) == 0:
            return []
        # Two pointer techique
        i = 0
        while i < len(a) and a[i] < 0:
            i += 1
        j = i
        i -= 1

        while i >= 0 and j < len(a):
            if a[i] ** 2 < a[j] ** 2:
                b.append(a[i] ** 2)
                i -= 1
            else:
                b.append(a[j] ** 2)
                j +=1
        if i < 0:
            b += list(map(self.square,a[j:]))
        elif j == len(a):
            b += list(map(self.square, a[i::-1]))

        return b