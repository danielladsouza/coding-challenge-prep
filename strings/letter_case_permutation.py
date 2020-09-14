from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = [""]
        
        #1 Iterate over the string S
        for i in range(len(S)):
            tmp_result = []
            # 2. Update the resulting strings
            for j in range(len(result)):
                if S[i].isalpha():
                    tmp_result.append(result[j] + S[i].lower())
                    tmp_result.append(result[j] + S[i].upper())
                else:
                    tmp_result.append(result[j] + S[i])
                
            result = tmp_result
        return result


s = Solution()
result = s.letterCasePermutation('a1b2')
print(result)