def Partition(arr, low, high):
    i = (low-1)        
    pivot = arr[high] 
    for j in range(low, high):

        if arr[j] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
def QuickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = Partition(arr, low, high)
 
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)
    if arr==sorted(arr):
        return arr
 

def get_data_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for item in lines:
            data_test_array=item.split()
        test_array=[int(x) for x in data_test_array]
        return test_array

n=len(get_data_file('data_test1.txt'))
print(QuickSort(get_data_file('data_test1.txt'),0,n-1))
