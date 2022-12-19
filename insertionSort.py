import time
arr=[]
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1]=arr[j-1], arr[j]
            j-=1
if __name__ == "__main__":
    for i in range(8):
        x = int(input(''))
        arr.append(x)
    # arr = [5,4,1,8,7,2,6,3]
    start = time.time()
    insertionSort(arr)
    print(arr)
    end = time.time() - start
    print('время: ',end)
