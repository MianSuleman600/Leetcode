class Solution:
    def __init__(self ):
        self.num = []
        self.target = 0

    def TwoSum(self,num,target):
        self.num = num 
        self.target= target

        for i in range(len(self.num)):
            for j in range(i+1,len(self.num)):
                if self.num[i] + self.num[j] == self.target:
                    return [i,j]
                
x = Solution()

result = x.TwoSum([2,7,11,15],9)
print(result)   

            
  


       
       
        






        