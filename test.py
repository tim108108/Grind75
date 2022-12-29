class Solution(object):
    def maxArea(self, height):
        res=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                print(height[i],height[j])
                k = (j-i)*min(height[i],height[j])
                if k>res:
                    res=k
        print(res)
        return res
height = [1,1]
Solution().maxArea(height)