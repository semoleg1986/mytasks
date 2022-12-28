num = [1, 2, 2, 4, 4, 1]
for i in range(len(num)):
    if i<len(num)-1:
        m=num[i]-num[i+1]
        if m>0:
            print(num[i])
            print(i)
