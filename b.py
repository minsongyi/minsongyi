a = int(input())
flag=0
def fac(k):
    global flag
    res = 0
    if k == 1:
        res = 1
    else:
        res = fac(k-1) * k
        #
    if flag= :
        print(res,'r')
    return res

fac(a)# 함수 내부에서 답만 프린트(다른 프린트문 없이)