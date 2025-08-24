class Solution(object):
    def longestConsecutive(self, nums):
        if not len(nums):
            return 0        
            # every sequence will have the starting point so i'll take advantage of that sating pointing and go futher
        # eg: if i found 3 then i'll look for 3-=2 in the set if that 2 is present then 3 is definetly not the starting point which means i'll stop wasting my time and go further to next element in the array

        # if there is no 2 in the set then 3 is that stating point so i'll starting seeing for next 4,5 6 ..consecutive elements and keep incerementing the cnt varibale

        # take a set and store all the elements in set as there are dups
        st=set()
        cnt=0
        longest_conse_seq=0
        for num in nums:
            st.add(num)
        # O(N) as each insertion in set takes 0(1) in average
        for num in st:
            if num-1 not in st:
                # nums[i] is the starting element
                # so go looking for n+1 elements
                seq_start=num
                cnt=1
                # in worst case itself the inner loop run only n times for the entire algo itself so it is amortized O(N)
                while seq_start+1 in st:
                    seq_start+=1
                    cnt+=1
                longest_conse_seq=max(longest_conse_seq,cnt)
        return longest_conse_seq      





        