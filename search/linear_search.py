arr_user = [10, 1, 16, 2, 11, 5, 9, 13, 7]
find_user = 11

def linear_search(arr, find):
  index=0
  for i in arr:
    if find==i:
      return f"{i} elementi {index}-indexda turibdi."
    index+=1
  return f"{i} elementi topilmadi."

print(linear_search(arr=arr_user, find=find_user))
