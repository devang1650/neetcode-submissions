class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                    break
            
        #     if nums[left]+nums[right]==target:
                
        #         break
        #     if nums[left]+nums[right]>target:
        #         right-=1
        #     if nums[left]+nums[right]<target:
        #         left+=1
        # return [left , right]