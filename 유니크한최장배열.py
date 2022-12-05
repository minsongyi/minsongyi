# class Solution1:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         ans=0
#         n=len(s)
#         if n==1:
#             ans=1
#         elif n==2:
#             if s[0]==s[1]:
#                 ans=1
#             else:
#                 ans=2
#         elif n==3:
#             if s[0]==s[1]==s[2]:
#                 ans=1
#             elif s[0]!=s[1]and s[1]!=s[2] and s[0]!=s[2]:
#                 ans=3
#             else:
#                 ans=2
#         return(ans)
#문자 길이가 3 이하일때 모든 경우 실행
from traceback import print_list


class Solution2:
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        overlap=0
        left=0
        right=0
        an=0
        for i in range(0,n):
            for j in range(i,n):
                left=i
                right=j
                
                for k in range(i,j+1):
                    overlap=0
                    
                    for w in range(i,j+1):
                        if s[k]==s[w]:
                            overlap+=1
                            
                    if overlap>1:#중복 발견
                        break
                if overlap==1:        
                    if (j-i)+1>an:
                        an=(j-i)+1
                        #print(i,j,an)
        return(an)
        
# solution2=Solution2()      



# result=solution1.lengthOfLongestSubstring("pwwkew")
# print(result)

# #만약 left right이 주어졌을때 1.돌려보면서 중복이있는지  2중포문사용.
# #left랑 right의 모든경우를 알아내는 방법 left는 0보다크고 문자열길이보단 작아야되고 right은 left보다는 크거나 같고 문자열길이보단 작아야한다



class Solution3:
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        overlap=0
        left=0
        right=0
        an=0
        H=[0]*max(s)
        for i in range(0,n):
            for j in range(i,n):
                left=i
                H=[0]*max(s)
                
                #이중포문보다 빠르게 중복판단
                for k in range(left,right+1):
                    H[k]+=1
                    
                for w in range(0,len(H)):
                    if H[w]>1:
                        return(an)
                    else:
                        continue
                an=(right-left+1)
    
        return(an)
        
solution3=Solution3()      



result=solution3.lengthOfLongestSubstring("pwwkew")
print(result)