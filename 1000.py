A,B= [*map(int, input().split(' '))]

def add(A,B):
    answer= A+B
    return answer

def minus(a,b):
    answer= a-b
    return answer


def multiply(a,b):
    answer= a*b
    return answer


def divide(x,y):
    return(x//y)


def di(a,b):
    return(a%b)


print(add(A,B))
print(minus(A,B))
print(multiply(A,B))
print(divide(A,B))
print(di(A,B))
    