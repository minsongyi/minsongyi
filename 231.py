'''
import time

n= int(input())

def f(x):
    global n
    # time.sleep(1)
    # print(x)
    if x>=-1:
        if x==-1:
            x=1/2
        if 2*x==n:
            return True
            
        elif 2*x<n:
            return f(2*x)
            
        elif 2*x>n:
            return False
    else:
        if 1/2*x==n:
            return True
            
        elif 1/2*x<n:
            return f(1/2*x)
            
        elif 1/2*x>n:
            return False
print(f(-2**32))


'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        answer = self.recursion( n )
        return answer
        
    def recursion(self, k):
        if k == 0:
            return False
        if k == 1: 
            return True
        
        #  여기 채우기.  self.discriminate( ? ) 재귀써서 풀기
        if k%2==1:
            return False
        elif k//2==1:
            return True
        else:
            k= k//2
            return self.recursion(k)
                
            

        return 