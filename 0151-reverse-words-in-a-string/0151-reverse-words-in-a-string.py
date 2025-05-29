class Solution(object):
    def reverseWords(self, s):
        def remove_unwanted_space(s):
            n = len(s)
            left, right = 0, n - 1  # corrected from n to n-1 for valid indexing
            
            # edge case what if s="  " so left++ keeps on going so, see to that your inside the bound
            # step:1 remove leading spaces (keep going until you see a chr)
            while left <= right and s[left] == " ":
                left += 1
            # step:2 remove trailing spaces
            while left <= right and s[right] == " ":
                right -= 1  # changed += to -= to move backwards for trailing spaces
            
            if left > right:
                return ""  # bze if s="   " answer is "" not " "
            
            # now remove in between word spaces that are more than one
            # you need to have extra space(result list) becase you cannot handle string like list(in place) as string is immutable
            result = []
            while left <= right:
                if s[left] != " ":
                    # if char append and go forward
                    result.append(s[left])
                elif s[left] == " " and result[-1] != " ":
                    # if single space append and go forward
                    result.append(s[left])
                left += 1
            return result

        def reverse_result(a):
            n = len(a)
            left, right = 0, n - 1
            while left < right:
                a[left], a[right] = a[right], a[left]  # fixed swap here
                left += 1
                right -= 1
            return a

        def reverse(l, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        def reverse_by_word(c):
            start = 0
            n = len(c)
            while start < n:
                end = start
                while end < n and c[end] != " ":  # fixed condition from 'end != " "'
                    end += 1
                reverse(c, start, end - 1)
                start = end + 1
            return " ".join(c)

        # start here
        a = remove_unwanted_space(s)
        if a == "":
            return ""
        b = reverse_result(a)
        return reverse_by_word(b)
