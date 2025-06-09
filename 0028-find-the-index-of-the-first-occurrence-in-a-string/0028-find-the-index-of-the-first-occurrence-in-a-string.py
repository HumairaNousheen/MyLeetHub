class Solution(object):
    def strStr(self, haystack, needle):
        # Edge case: if needle is empty
        if not needle:
            return 0

        def LPS(pattern):
            m = len(pattern)
            lps = [0] * m
            length = 0  # length of the previous longest prefix suffix
            i = 1

            while i < m:
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

        def KMP(text, pattern):
            n = len(text)
            m = len(pattern)
            lps = LPS(pattern)
            i = j = 0  # i -> text, j -> pattern

            while i < n:
                if text[i] == pattern[j]:
                    i += 1
                    j += 1

                if j == m:
                    return i - j  # pattern found at index i-j
                elif i < n and text[i] != pattern[j]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return -1  # pattern not found

        return KMP(haystack, needle)
