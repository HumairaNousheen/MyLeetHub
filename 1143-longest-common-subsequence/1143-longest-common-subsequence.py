class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
       # dp using memoization 
        def LCS(i, j, memo):
            # Base case: if either of the  string is empty
            if i == -1 or j == -1:
                return 0
            
            # If already computed, return stored value
            if memo[i][j] != -1:
                return memo[i][j]
            
            # If characters match
            if text1[i] == text2[j]:
                memo[i][j] = 1 + LCS(i-1, j-1, memo)
                return memo[i][j]
            else:
                memo[i][j] = max(LCS(i-1, j, memo), LCS(i, j-1, memo))
                return memo[i][j]
            
       

        n = len(text1)
        m = len(text2)
        # Initialize memoization table with -1
        memo = [[-1 for _ in range(m)] for _ in range(n)]
        return LCS(n-1, m-1, memo)