A='어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
B='"재귀함수가 뭔가요?"'
C1='''"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'''
C2='마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
C3='''그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'''
D='"재귀함수는 자기 자신을 호출하는 함수라네"'
E='라고 답변하였지.'
ss='----'
a=int(input())

def what_is_rec(n):
    print('_'*(4*n-4)+B)
    
def tell_story(n):
    print('_'*(4*n-4)+C1)
    print('_'*(4*n-4)+C2)
    print('_'*(4*n-4)+C3)
    
def he_ans(n):
    print('_'*(4*n-4)+E)
    
def f(n):
    what_is_rec(n)
    
    if n==(a+1):
        print('_'*(4*n-4)+D)
        he_ans(n)
        return

    tell_story(n)
    f(n+1)
    he_ans(n)

print(A)
f(1)
