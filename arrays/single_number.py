from collections import defaultdict


class Solution:
    def singleNumber_1(self, nums: List[int]) -> int:
        """
        Brute Force Solution
        Counter
        T.C. - O(2N)
        S.C. - O(N)

        nums = [2,2,1]

        if k in counter:
            pop counter[k]
        """
        num_counter = defaultdict(bool)

        for n in nums:
            if n in num_counter:
                del num_counter[n]
            else:
                num_counter[n] = True

        return next(iter(num_counter.keys()))

    class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            """
                Use chain of XORs to identify the single number that has not been
                duplicated

                XOR of two identical numbers yields a 0
                XOR of 0 and a single number yields the single number
                T.C. - O(N)
                S.C. - O(1)
            """
            out = 0
            for n in nums:
                out = out ^ n

            return out