 def runningSum(self, nums: List[int]) -> List[int]:
        #initialize variables 
        rs = [0] * (len(nums)) 
        rs[0] = nums[0]
        
        #calculate and return running sum 
        for i in range(1,len(nums)):
            rs[i] = rs[i-1] + nums[i]
        return rs
            