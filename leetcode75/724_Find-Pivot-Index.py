def pivotIndex(self, nums: List[int]) -> int:
    #initialize variables 
    rightSum = 0
    leftSum = 0 
    
    #calculate the right sum by calculating sum of array 
    for i in range(len(nums)): 
        rightSum = rightSum + nums[i]
    
    for i in range(len(nums)): 
        rightSum = rightSum - nums[i]
        
    #find pivot index 
        if leftSum == rightSum: 
            return i
        
        leftSum = leftSum + nums[i]
        
    #if no pivot index exists 
    return -1