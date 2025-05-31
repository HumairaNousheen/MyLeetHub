class Solution(object):
    def longestPalindromeSubseq(self, s):
        # a subsequence or substring can be continuous or non-contiguous
        # follow the same approch you did for LCS problem
        # just take another variable b and reverse s and store it in b

        def LPS(memo, s_len, r_len, r):
            # base case when index is -1 return back
            if s_len < 0 or r_len < 0:
                return 0
            # if already found in memo don't recompute overlapping subproblem, just return it from the memo
            if memo[s_len][r_len] != -1:
                return memo[s_len][r_len]
            # if there is a match of a string shrink the size     
            if s[s_len] == r[r_len]:
                memo[s_len][r_len] = 1 + LPS(memo, s_len - 1, r_len - 1, r)
                # store it in memo 
                return memo[s_len][r_len]
            else:
                memo[s_len][r_len] = max(LPS(memo, s_len, r_len - 1, r), LPS(memo, s_len - 1, r_len, r))   
                return memo[s_len][r_len]

        s_len = len(s)
        r = s[::-1]
        r_len = len(r)
        memo = [[-1 for _ in range(r_len)] for _ in range(s_len)]

        return LPS(memo, s_len - 1, r_len - 1, r)
