class Solution(object):
    def maxSubArray(self, nums):
        # Initialize subarr_sum with the first element and max_sum with the first element
        subarr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            subarr_sum += nums[i]  # Add the current element to subarr_sum

            # If subarr_sum becomes negative, reset it to 0
            if subarr_sum < 0:
                subarr_sum = nums[i]  # Start fresh from the current element, not zero

            # Update max_sum if subarr_sum is larger
            if subarr_sum > max_sum:
                max_sum = subarr_sum

        return max_sum












   #optimal approch----kadens algorithm
        #have 2 varibale called sum and max_sum
        #traverse the array and keep incrementing the sum 
        # when your sum becomes neagtive,simply drop your sum and start it again from the next value
        # as you loop keep checking if your sum is greater than your max_sum if so, update your max_sum and move forward ,because your futhure elements may impact your sum by some negative value 