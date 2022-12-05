a= int(input())

def multiply(a,b):
    answer= a*b
    return answer


for i in range(1,1+9):
    an=multiply(a,i)
    print(str(a)+' '+'*'+' '+str(i)+' '+'='+' '+str(an))