# Explanation of the solution - https://docs.google.com/presentation/d/1Th9U7Cwrk4ti-rRlw6iM1zsTID0_AuZxMFkgW2s2VaE/edit?usp=sharing

class Solution():
    def quotient(self, a:int, b:int) -> int:
        print(bin(a), bin(b))
        a_neg = False
        b_neg = False

        x = a
        if a < 0:
            x = ~a
            a_neg = True

        y = b 
        if y < 0:
            y = ~b
            b_neg = True

        if y == 0:
            raise Exception('Divide by 0')

        if y == 1:
            return x

        q, k = 0, 32
        y_shifted = y << k
        while x >=  y:
            #print(x, q)
            while y_shifted > x:
                y_shifted >>= 1
                k -= 1
            x -= y_shifted
            q += 1 << k
            #print(x, q, k)

        if a_neg and not b_neg:
            q = -q
        return q

s = Solution()
result = s.quotient(-7, 3)

print(result)
