class Solution(object):
    def isAnagram(self, s, t):

        # can also take advantage of sorting but takes nlog time complexity
        if len(s) != len(t):
            return False
        
        count = [0] * 26  # fixed size array for 'a' to 'z' so constant space complexity

        for ch1, ch2 in zip(s, t):
            count[ord(ch1) - ord('a')] += 1
            count[ord(ch2) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
