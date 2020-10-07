# 509. Fibonacci Number

class Solution:
    def fib(self, N: int) -> int:
        # [0,1,2,3,4,5]
        # [0, 1, 0 + 1, 0 + 1 + 1, 0 + 1 + 1 + 0 + 1,  0 + 1 + 1 + 0 + 1 + 0 + 1 + 1]
       
        if N <= 1:
            return N
        
        fminus_1, fminus_2 = 1, 0
        result = 0
        
        # Taken care of fib(0), fib(1)
        # Run for N-1 iterations..
        # Calculate Fib{1}  .. Fib[N-1]
        # Fib[N] = Fib[N-1] + Fib[N-2]
        for _ in range(1, N):   # Number of iterations
            result = fminus_1 + fminus_2   
            fminus_1, fminus_2 = result, fminus_1  

        return result

s = Solution()
result = s.fib(2)
print(result)