'''
1. 가장 점수가 높은 5개의 문제의 합 
2. 가장 점수가 높은 5개의 문제의 번호

- 붙여서 sort 해서 가장큰 5개의 값 구하기
'''
L=[]
A=[]
an=0
AN=[]
for i in range(0,8):
    a= int(input())
    L.append(a)
for i in range(0,8):
    A.append(-L[i])
A.sort()
for i in range(0,5):
    an+=-A[i]
print(an)
for k in range(0,5):
    for i in range(0,8):
        if -A[k]==L[i]:
            AN.append(i+1)
AN.sort()
print(*AN)