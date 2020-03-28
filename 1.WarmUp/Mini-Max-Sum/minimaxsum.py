def miniMaxSum(arr):
    sum_arr = []
    x = " "
    for item in arr:
        sum_arr.append(sum(arr) - item)
    print(min(sum_arr),max(sum_arr))

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    miniMaxSum(arr)