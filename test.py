class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        tmp=[]
        for i in range(len(nums)-1):
            j=i+1
            k=len(nums)-1
            if i>0 & nums[i]==nums[i-1]:
                continue
            while k>j:
                if nums[i]+nums[j]+nums[k] > 0 :
                    k-=1
                elif nums[i]+nums[j]+nums[k] < 0 :
                    j+=1
                else :
                    tmp.append([nums[i],nums[j],nums[k]])
                    k-=1
                    j+=1
            print(tmp)
        return tmp
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
n=[-1,0,1,2,-1,-4]
n1=[0,0,0]
Solution().threeSum(n)