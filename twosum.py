class Solution(object):
    def twoSum(self, nums, target):
        L=[]
        H=[-1]*10001
        for i in range(0,len(nums)):
           H[nums[i]]=i
           
        for i in range(len(H)):
            if H[i]!=-1:
                L.append(i)
        return(L)
a=Solution()
print(a.twoSum([3,2,4],6))