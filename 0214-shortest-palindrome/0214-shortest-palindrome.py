class Solution(object):

    # use same KMP logic with LPS
    def compute_lps(self, pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def shortestPalindrome(self, s):
        if not s or len(s) == 1:
            return s
        
        rev_s = s[::-1]
        temp = s + '#' + rev_s
        lps = self.compute_lps(temp)
        to_add = rev_s[:len(s) - lps[-1]]
        return to_add + s
