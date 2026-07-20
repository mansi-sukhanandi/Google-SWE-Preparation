# Problem: Max Consecutive Ones (Easy)
# Time Complexity: O(n)
# Space Complexity: O(1)
def max_consecutive(num):
    current_count = 0
    max_count = 0
    for n in num :
        if n == 1:
            current_count += 1
            if current_count > max_count :
                max_count = current_count
        else :
            current_count = 0

    return max_count

test_array = [1,1,0,1,1,1,1]
print("Result :",max_consecutive(test_array))
