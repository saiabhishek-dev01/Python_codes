class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uq=set()
        p=0
        for j in range(len(nums)): 
            if nums[j] not in uq:
                uq.add(nums[j])
                nums[p]=nums[j]
                p+=1

        return p

        