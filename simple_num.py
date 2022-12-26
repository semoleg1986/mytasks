import time
start = time.time()

n = int(input("n="))
simple_nums=[]
for i in range(2, n+1):
    # print(i)
    for j in simple_nums:
        # print(i)
        print(simple_nums)
        if i % j == 0:
            # print("yes")
            break
    else:
        # print(i)
        simple_nums.append(i)
# print (simple_nums)

end = time.time() - start
print('время: ',end)
