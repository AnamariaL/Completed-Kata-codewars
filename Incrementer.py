def incrementer(nums):
    x=1
    for i in range(len(nums)):
       nums[i] += x
       if nums[i] >=10:
          nums[i] =nums[i]% 10
       x+=1
    return nums  