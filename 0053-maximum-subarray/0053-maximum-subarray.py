class Solution:
    def maxSubArray(self, nums):
        # Initialize sum and maxi with appropriate values
        sum = 0
        maxi = -200000 # Using negative infinity to represent the smallest possible value
        
        for x in range(len(nums)):
            sum += nums[x]  # Add the current element to the sum

            if sum > maxi:
                maxi = sum  # Update maxi if the current sum is larger

            if sum < 0:
                sum = 0  # Reset sum if it becomes negative

        return maxi











   #optimal approch----kadens algorithm
        #have 2 varibale called sum and max_sum
        #traverse the array and keep incrementing the sum 
        # when your sum becomes neagtive,simply drop your sum and start it again from the next value
        # as you loop keep checking if your sum is greater than your max_sum if so, update your max_sum and move forward ,because your futhure elements may impact your sum by some negative value 