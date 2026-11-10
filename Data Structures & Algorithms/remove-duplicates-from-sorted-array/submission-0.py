class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Scan the array from left to right
        For every new unique number you encounter:
        keep it
        For every duplicate:
        skip or overwrite depending on your method
        Count how many unique numbers you kept
        that count is returned as k
        you need two positions (one reading, one writing)
        you need to overwrite the array as you go
        """

        i = 1
    
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        return i

