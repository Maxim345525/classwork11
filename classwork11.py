def ex_2(arr, digit):
    count = 0
    for i in arr:
        count += len(re.findall(digit, i))
    return f'Count = {count}'
