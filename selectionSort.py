import time
arr=[]
def selectionSort(arr):
   for i in range(len(arr)-1,0,-1):
       maxpos=0
       # print(i)
       for j in range(1,i+1):
           # print(j)
           if arr[j]>arr[maxpos]:
               maxpos = j
               # print(maxpos)
       temp = arr[i]
       arr[i] = arr[maxpos]
       arr[maxpos] = temp
if __name__ == "__main__":
    start = time.time()
    for i in range(8):
        x = int(input(''))
        arr.append(x)
    # arr = [5,4,1,8,7,2,6,3]
    selectionSort(arr)
    print(arr)
    end = time.time() - start
    print('время: ',end)
