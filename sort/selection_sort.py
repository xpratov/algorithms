arr_user = [10, 1, 16, 2, 11, 5, 9, 13, 7]

def selection_sort(arr, size):
  for s in range(size):
    min_idx = s
    for i in range(s + 1, size):
      if arr[i] < arr[min_idx]:
        min_idx = i
    (arr[s], arr[min_idx]) = (arr[min_idx], arr[s])
  return arr

print(selection_sort(arr_user, len(arr_user)))