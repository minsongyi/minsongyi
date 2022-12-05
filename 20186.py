'''
N개의 자연수가 좌우로 배열되어 있다. 여러분은 이 중 K개를 골라야 한다. 고를 때는 K개 모두를 한번에 골라야 한다.
저수 계산 바법= 내기 보는수 - (지금 보고 잇는 수에 순서 -1 )

N개의 자연수 배열과 양의 정수 K가 주어질 때, 전체점수의 최댓값을 출력하는 프로그램을 작성하시오.


가장 큰거 부터 골라서 계산

'''
n, k =[*map(int, input().split(' '))]
A= [*map(int, input().split(' '))]
an=0
for i in range(1,k+1):
    an+= max(A)-(i-1)
    A.remove(max(A))
    n-=1
    #print(i, an)
print(an)