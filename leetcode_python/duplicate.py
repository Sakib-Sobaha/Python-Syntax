class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for x in nums:
            if nums.count(x) > 1:
                return True 
        return False
print(Solution().containsDuplicate([1,2,3,4]))

