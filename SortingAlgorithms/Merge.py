def Merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    Left = [0] * (n1)
    Right = [0] * (n2)
    for i in range(0, n1):
        Left[i] = arr[l + i]
    for j in range(0, n2):
        Right[j] = arr[m + 1 + j]
    i = 0     
    j = 0     
    k = l     
    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = Left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = Right[j]
        j += 1
        k += 1
  
def MergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        MergeSort(arr, l, m)
        MergeSort(arr, m+1, r)
        Merge(arr, l, m, r)
    if arr==sorted(arr):
        return arr

def get_data_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for item in lines:
            data_test_array=item.split()
        test_array=[int(x) for x in data_test_array]
        return test_array
 

n=len(get_data_file('data_test5.txt'))
print(MergeSort(get_data_file('data_test5.txt'),0,n-1))