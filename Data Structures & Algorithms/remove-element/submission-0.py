class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Scan the array
        check if any of the elements in the array is the same as the val given
        if it is remove it from the array
        then count the number of elements remaining in the array
        and return that as k
        p.s: since this is a in-place problem i'll be using a two pointer approach to solve it
        """

        i = 0
    
        for j in range(len(nums)):   #getting the index instead of value
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i