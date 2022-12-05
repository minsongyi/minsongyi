def number(a,b):
    return a*b


def solve_2557():
    def world():
        return'Hello World!'
    print(world())
    return 



def solve_10950():
    g= int(input())
    def plus(a,b):
        return a+b
    for i in range(0,g):
        t= [*map(int, input().split(' '))]
        print(plus(t[0],t[1]))
    return


def plus(a,b):
    return a+b


def solve_10951():
    while True:
        t= [*map(int, input().split(' '))]
        if plus(t[0],t[1])==0:
            break
        else:
            print(plus(t[0],t[1]))
            
            
def solve_10998():
    t= [*map(int, input().split(' '))]
    print(number(t[0],t[1]))
    
    
def ask(a):
    return ord(a)


def solve_11654():
    a= input()
    print(ask(a))
    
    
def big(a,b):
    if a>b:
        return '>'
    elif a<b:
        return '<'
    elif a==b:
        return'=='
    
    
def solve_1330():
    t= [*map(int, input().split(' '))]
    print(big(t[0],t[1]))
    
    
def repeat():
    t= input().split(' ')
    an=''
    for i in range(0, len(t[1])):
        for k in range(0, int(t[0])):
            an+=t[1][i]
    print(an)
        
        
def solve_2675():
    a= int(input())
    for i in range(0,a):
        repeat()
        
        
def solve_10818():
    a= int(input())
    t= [*map(int, input().split(' '))]
    print(min(t), max(t))
    
    
def solve_11720():
    a= int(input())
    b= input()
    an=0
    for i in range(0,a):
        an+=int(b[i])
    print(an)


def solve_8958():
    a= int(input())
    for i in range(0,a):
        b= input()
        s=0
        an=0
        for k in range(0, len(b)):
            if b[k]=='O':
                s+=1
                an+=s
            elif b[k]=='X':
                s=0
                an+=s
        print(an)
solve_2675()
    