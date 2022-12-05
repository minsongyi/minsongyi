a= input()
a=a.split(' ')
L=[]
ply_n=int(a[0])
ply_l=int(a[1])
for i in range(0,ply_l):
    b= input()
    b=b.split(' ')
    L.append(b)



B=[]
for i in range(0, ply_n+1):
    B.append([])

for g in range(0, ply_l):
   # print(int(L[g][1]),'*')
    B[int(L[g][1])].append(L[g][2])
#print(B)

for h in range(1,len(B)): 
    if len(B[h])%2==1:
        #print('y')
        print('NO')
        exit(0)
              ### 1번째부터 검사하면 B[h] 가 0 1 0 1 인 경우 두번째 1부터 검사를 시작할텐데 이상하다.
    if  len(B[h])%2==0: 
        if B[h]==['0','1']*(len(B[h])//2):      ### len(B) 길이가 6이면, 두 개 씩 끊어서 0 1 인지 검사해야겠다
            continue
        else:
            print('NO')
            exit(0)
    else:
        print('NO')
        exit(0)
               ### 두개씩 검사하는 거니까 for h in range(0,len(B), 2): 
                         ### B[h] == '0' B[h + 1] == '1
                                ### 근데 B의 길이가 홀수라면 오류가 나지 않을까. 좀 생각해 봐야겠다.

A=[]
for i in range(0,ply_n):
    A.append([])

for k in range(0,ply_l):
    A[int(L[k][1])-1].append(int(L[k][0]))

#print(A)
an=0

#print(A, B)

for q in range(0,ply_n):
    for f in range(0, len(A[q])):
        if f%2==0:                ### 모든 짝별로 검사해야하는데 f == 0 일때만 시작 시간으로 취급했다
            an= A[q][f]
        else:
            an= an-A[q][f] 

            if abs(an)<60:              
            # print(an)
                print('NO')
                exit (0)

            
print('YES')               

'''

이런 예시도 잘 될 지 해봐야 겠다.

1 4
0 1 0
60 1 1
120 1 0
180 1 1


답 : YES



3 12
100 1 0
200 3 0
300 2 0
400 1 1
500 2 1
600 3 1
1100 1 0
1200 3 0
1300 2 0
1400 1 1
1500 2 1
1600 3 1


'''