arr_user = [10, 1, 16, 2, 11, 5, 9, 13, 7]

def merge(x, y):
  p1 = p2 = 0
  out = []
  while p1 < len(x) and p2 < len(y):
    if x[p1] < y[p2]:
      out.append(x[p1])
      p1 += 1
    else:
      out.append(y[p2])
      p2 += 1
  out += x[p1:] + y[p2:]
  return out

def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  if len(arr) == 2:
    return sorted(arr)
  mid = len(arr) // 2
  return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

print(merge_sort(arr_user))