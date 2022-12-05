def is_same(s,left,right):
    # if left+1==right or left==right:
    #     return True
    return right-left<=1 or (s[left]==s[right] and is_same(s,left+1,right-1)) 
    # if s[left]==s[right]:
    #     return is_same(s,left+1,right-1)
    # else:
    #     return False
def is_p(s, left, right):
    if left+1==right or left==right:
        return 1
    if s[left]==s[right]:
        return is_p(s,left+1,right-1)+1
    else:
        return 0
# n= int(input())
# for i in range(0,n):
#     s=input()
#     print(1 if is_same(s,0,len(s)-1) else 0)
print(max(is_p('abc',0,2)-1,0))