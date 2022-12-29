class Solution(object):
    def sortColors(self, nums):
        head = 0
        tail = len(nums)-1
        i = 0
        while i <= tail:
            if nums[i] ==0:
                nums[head], nums[i] = nums[i], nums[head]
                head+=1
                i+=1
            elif nums[i]==1:
                i+=1
            elif nums[i]==2:
                nums[tail], nums[i]=nums[i], nums[tail]
                tail-=1
        return nums
nums = [2,0,2,1,1,0]
Solution().sortColors(nums)