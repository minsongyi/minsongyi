'''
사전순으로 가장 앞
2개- BB
4개- AAAA
6개- AAAABB
8개- AAAAAAAA
10개- AAAAAAAABB
 4의 배수가 아닐떄에는 끝에 b가 있다
 2의 배수가 아닐떄에는 -1 을 출력
 .은 모든 요소 사이에 넣기
'''
a= input().split('.')

L=[]
AN=''
an=0
for i in range(0,len(a)):
    if len(a[i])%2!=0:
        print('-1')
        exit()
    else:
        L.append(len(a[i]))
        #print(L)
for k in range(0,len(L)):
    if L[k]%4!=0:
        AN+=((L[k]//4)*'AAAA'+'BB')

    elif L[k]%4==0:
        AN+=((L[k]//4)*'AAAA')
    
    elif L[k]==2:
        AN+=('BB')

    if an!=len(L)-1:
        AN+=('.')
        an+=1
    
print(AN)