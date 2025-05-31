class Solution(object):
    def isSubsequence(self, s, t):
        # Identify smaller and larger strings
        smaller = s
        larger = t
        m = len(smaller)
        n = len(larger)

        # Memo table: initialize with -1
        memo = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        # Recursive function with memoization
        def dp(i, j):
            # If smaller string is fully matched
            if j == 0:
                return True
            # If larger string is exhausted but smaller isn't
            if i == 0:
                return False

            if memo[i][j] != -1:
                return memo[i][j]

            if larger[i-1] == smaller[j-1]:
                memo[i][j] = dp(i-1, j-1)
            else:
                # no need to split call as here you just need to find if smaller sting is fully present in larger sting irrespective of contiguous not to find if there is any common subseq as u did in LCS  but check if s is fully present in t
                # so if not match stand at s and then shrink your t 
                memo[i][j] = dp(i-1, j)

            return memo[i][j]

        return dp(n, m)
