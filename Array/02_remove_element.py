# Problem: Remove Element (Easy)
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_element(nums , val):
    pointer = 0
    for num in nums :
        if num != val :
            nums[pointer] = num
            pointer += 1

    return pointer

test = [5,6,5,5]
print("Result :",remove_element(test,5))
