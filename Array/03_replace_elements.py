def replace_element(nums):
    max_so_far = -1
    for i in range(len(nums)-1,-1,-1) :
        temp = nums[i]
        nums[i] = max_so_far
        if temp > max_so_far :
            max_so_far = temp

    return nums

test = [17,18,5,4,6,1]
print("Result :",replace_element(test))
