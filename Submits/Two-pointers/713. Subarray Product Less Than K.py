class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        left, product = 0, 1
        
        for right in range(len(nums)):
            product *= nums[right]
            while (product >= k and left <= right):
                product //= nums[left]
                left += 1
                 
            count += (right - left + 1)
                
        return count
        
'''
Time Complexity - O(N^2)
Space Complexity - O(1)
'''
