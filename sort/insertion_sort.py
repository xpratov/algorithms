arr_user = [10, 1, 16, 2, 11, 5, 9, 13, 7]

def insertion_sort(arr):  
  for i in range(1, len(arr)):  
    a = arr[i]  
    j = i - 1  
    while j >= 0 and a < arr[j]:  
      arr[j + 1] = arr[j]  
      j -= 1  
    arr[j + 1] = a  
      
  return arr  
      
 
print(insertion_sort(arr_user))