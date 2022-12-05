a= input()
a=a.split(' ')
A=int(a[0])
B=int(a[1])
V=int(a[2])
ans = 1
V  = V - A

X = A - B


ans += (V-1) // X  +1

print(ans)