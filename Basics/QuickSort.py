def QuickSort(arr,low,high):

    if(low<high):
        i = low + 1 
        j = high
        pivot = arr[low]

        while(True):

            while(i <= high and arr[i] < pivot):
                i += 1

            while(j >= low and arr[j] > pivot):
                j -= 1

            if(i < j):
                arr[i],arr[j] = arr[j],arr[i]
            else:
                break
            
        arr[low],arr[j] = arr[j],arr[low]

        QuickSort(arr,low,j-1)
        QuickSort(arr,j+1,high)
        
    return arr

arr = [10,90,32,21,3423]
low = 0
high = len(arr) - 1

ans = QuickSort(arr,low,high)
print(ans)



