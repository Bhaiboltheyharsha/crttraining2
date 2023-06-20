def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]

    left_arr=[i for i in arr[1:] if i<=pivot]
    right_arr=[i for i in arr[1:] if i>pivot]

    return quicksort(left_arr)+[pivot]+quicksort(right_arr)
n=[30,10,20,20,40,50]
res=quicksort(n)
print(res)
