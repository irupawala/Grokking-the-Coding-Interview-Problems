class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        i = 0
        result = None
        smallest_diff = float('inf')
        
        for i in range(0, len(nums)-2):
            
            # update: ignore the duplicate numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue              
            
            left = i+1
            right = len(nums)-1
            
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]

                if _sum == target:
                     return _sum

                diff = target - _sum
                if abs(diff) < smallest_diff:
                    smallest_diff = abs(diff)
                    result = _sum
                    
                if diff > 0:
                    left += 1
                else:
                    right -= 1
                
        return result
                
                
#S = Solution()
#print(S.threeSumClosest([-2, 0, 1, 2], 2))
#print(S.threeSumClosest([-3, -1, 1, 2], 1))                    
#print(S.threeSumClosest([1, 0, 1, 1], 100))                       
#print(S.threeSumClosest([-1,2,1,-4], 1))   
#print(S.threeSumClosest([0,0,0], 1)) 
#print(S.threeSumClosest([1,1,-1,-1,3], -1))
#print(S.threeSumClosest([0,2,1,-3], 1))

'''
Time Complexity - O(N.LogN + N^2)
Space Complexity - O(N) # required for sorting by few libraries
'''
