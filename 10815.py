n= int(input())
card=[*map(int, input().split(' '))]
m= int(input())
number=[*map(int, input().split(' '))]
Card={}
An=[]
for i in range(0,n):
    Card[card[i]]=i
for i in range(0,m):
    if number[i] in Card:
        An.append(1)
    else:
        An.append(0)
#print(Card)
print(*An)