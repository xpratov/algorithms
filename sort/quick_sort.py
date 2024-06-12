arr_user = [10, 1, 16, 2, 11, 5, 9, 13, 7]

def quick_sort(arr):
  if len(arr)<2:
    return arr
  else:
    pivot=arr.pop(len(arr)//2)
    kichik=[i for i in arr if i<=pivot]
    katta=[i for i in arr if i>pivot]
    return quick_sort(kichik)+[pivot]+quick_sort(katta)

print(quick_sort(arr_user))
