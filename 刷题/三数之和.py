class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # 对数组进行排序
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rt=[]
        n = len(nums)
        for i in range(n - 2):
           x=nums[i]
           if i>0 and x==nums[i-1]:
               continue
           if x+nums[i+1]+nums[i+2]>0:
               break
           #-2 和 -1 就可以表示 n-2 和 n-1
           if x+nums[-2]+nums[-1]<0:
               continue
           j=i+1
           k=n-1
           while j<k:
               s=nums[j]+nums[k]+x
               if s>0:
                   k-=1
               elif s<0:
                   j+=1
               else:
                   rt.append([x,nums[j],nums[k]])
                   j+=1
                   while j<k and nums[j]==nums[j-1]:
                       j+=1
                   k-=1
                   while j<k and nums[k]==nums[k+1]:
                        k-=1
        return rt