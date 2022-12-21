def mergeSort(arr):
    n=len(arr)
    if n>1:
        m = n//2
        l = arr[:m]
        r = arr[m:]
        mergeSort(l)
        mergeSort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

if __name__ == "__main__":
    arr = [5,4,1,8,7,2,6,3]
    mergeSort(arr)
    print(arr)
