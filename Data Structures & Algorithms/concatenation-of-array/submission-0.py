class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        take the original array
        duplicate it
        and return the new array
        """
        ans = []
        for i in nums:
            ans.append(i)
        ans = ans + nums

        return ans
