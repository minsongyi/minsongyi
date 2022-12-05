def solve_2753():
    a= int(input())
    if a%4==0 and a%100!=0:
        print(1)
    elif a%400==0:
        print(1)
    else:
        print(0)
        
def solved_2741():
    a= int(input())
    for i in range(1, a+1):
        print(i)
def solved_9498():
    a= int(input())
    if 90<=a and a<=100:
        print('A')
    elif 80<=a and a<=89:
        print('B')
    elif 70<=a and a<=79:
        print('C')
    elif 60<=a and a<=69:
        print('D')
    else:
        print('F')

def solved_10871():
    L=[]
    a,b =[*map(int, input().split(' '))]
    A=[*map(int, input().split(' '))]
    for i in range(0,a):
        if A[i]<b:
            L.append(A[i])
    print(*L)
def solved_2884():
    a,b =[*map(int, input().split(' '))]
    if b>=45:
        print(a, b-45)
    elif b<45:
        if a-1<0:
            a= 24
        print(a-1, 60-(45-b))
def solved_1152():
    a= input()
    a= a.split()
    print(len(a))
def solved_3052():
    L=[]
    for i in range(0,10):
        a= int(input())
        L.append(a%42)
    L= set(L)
    print(len(L))
def solved_2908():
    a,b =input().split(' ')
    a= a[2]+a[1]+a[0]
    b= b[2]+b[1]+b[0]
    if int(a)> int(b):
        print(a)
    elif int(a)< int(b):
        print(b)
def solved_1546():
    a= int(input())
    A=[*map(int, input().split(' '))]
    B=[]
    for i in range(0,a):
        B.append((A[i]/max(A))*100)
    print(sum(B)/a)
def solved_10809():
    L=[-1]*26
    a= input()
    for i in range(0,len(a)):
        if L[ord(a[i])-97]==-1:
            L[ord(a[i])-97]=i
    print(*L)
def solved_1157():
    a= input()
    a=a.lower()
    L=[0]*26
    for i in range(0, len(a)):
        L[ord(a[i])-97]+=1
        #print(L)
    an=''
    for k in range(0,len(L)):

        if L[k]==max(L):
            if an=='':
                an= chr(k+97).upper()
            else:
                print('?')
                exit()
    print(an)
        
        
solved_1157()
    