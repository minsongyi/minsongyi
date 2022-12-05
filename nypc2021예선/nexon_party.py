n= int(input())
b= (input())
a=[*map(int, b.split(' '))]
A=sum(a)
peongguuns=A//n
peongguunb=(A//n)+1
q=A%n
an=0
if peongguuns * n == A : # 소수점 없음
    for i in range(n):
        if a[i]>peongguuns:
            an+=(a[i]-peongguuns)
else:
    for r in range(0, n):
        if a[r]>peongguuns and a[r]>peongguunb:
            if q>0:
                q-=1
                an+=a[r]-peongguunb
            else:
                an+=a[r]-peongguuns
        elif a[r]==peongguuns:
            continue
        elif a[r]==peongguunb:
            q-=1

print(an)