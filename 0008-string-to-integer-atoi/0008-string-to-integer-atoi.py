class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        
        i, sign, res = 0, 1, 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        if s[i]=='-' or s[i]=="+":
            if s[i]=="-": sign=-1 
            i+=1
     
        #like s[i]-'0' in range(1 to 9) means it will ne integer(digit)
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit  # Temporarily allow large values
            
            # Clamp to INT_MAX/INT_MIN if out of bounds
            if res * sign > INT_MAX:
                return INT_MAX
            if res * sign < INT_MIN:
                return INT_MIN
            i += 1
        
        return res * sign





        