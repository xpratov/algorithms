arr_user = [10, 1, 16, 2, 11, 5, 9, 13, 7]

def bubble_sort(arr):    
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr
                
print(bubble_sort(arr_user))