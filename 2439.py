a= int(input())
for i in range(1,a+1):
    if a-i==0:
        print('*'*i)
    else:
        print((a-i-1)*' ','*'*i)
