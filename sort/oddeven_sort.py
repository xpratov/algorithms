arr_user = [10, 1, 16, 2, 11, 5, 9, 13, 7]

def oddeven_sort(arr, n): 
    isSorted = 0
    while isSorted == 0: 
      isSorted = 1
      for i in range(1, n-1, 2): 
        if arr[i] > arr[i+1]: 
          arr[i], arr[i+1] = arr[i+1], arr[i] 
          isSorted = 0
      for i in range(0, n-1, 2): 
        if arr[i] > arr[i+1]: 
          arr[i], arr[i+1] = arr[i+1], arr[i] 
          isSorted = 0
    return arr
 
print(oddeven_sort(arr_user, len(arr_user)))