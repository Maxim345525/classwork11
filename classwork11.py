def ex_3(arr):
    nums = [int(i) for i in arr]
    nums_sum = 0
    for i in nums:
        nums_sum += i
    mean = nums_sum / len(nums)
    return f'Sum = {nums_sum}, Arithmetical mean = {mean}'