def fourth_sum(nums, res , target, pos):
    
    if len(res) == 4 and sum(res) == target:
        print(res)
        

    for i in range(pos , len(nums)):
        res.append(nums[i]);
        fourth_sum(nums,res,target,pos+1)
        del res[-1]


fourth_sum(sorted([1,0,-1,0,-2,2]),[],0, 0)