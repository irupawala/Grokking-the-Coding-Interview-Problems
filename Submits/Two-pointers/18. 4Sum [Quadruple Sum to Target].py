
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        
        for i in range(len(nums)-3):
            
            if i > 0 and nums[i] == nums[i-1]: continue
            
            p1 = nums[i]
            t1 = target - p1
            sublist_p1 = [p1]
            
            for j in range(i+1, len(nums)-2):
            
                if j > i+1 and nums[j] == nums[j-1]: continue
                
                p2 = nums[j]
                t2 = t1 - p2
                sublist_p1.append(p2)

                left = j+1
                right = len(nums)-1

                while left < right:
                    if nums[left] + nums[right] == t2:
                        sublist_p1.append(nums[left])
                        sublist_p1.append(nums[right])
                        result.append(sublist_p1[:])
                        sublist_p1.pop()
                        sublist_p1.pop()
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1

                    if nums[left] + nums[right] < t2:
                        left += 1
                    else:
                        right -= 1

                sublist_p1.pop()   
        
        return result
                        
        
        
#S = Solution()
#print(S.fourSum([2,2,2,1,1,1,0,0,0,-2,-2,-2], 2))

'''
Time Complexity - O(N.logN + N^3)
Space Complexity - O(n) for sorting
'''
        
        
