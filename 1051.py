a,b= [*map(int, input().split())] 
L=[]
for i in range(0,a):
    q= [*map(int, input().split())] 
    L.append(q)
def is_same(lt_y,lt_x, rt_y,rt_x, lb_y,lb_x, rb_y,rb_x):
    global L
    if rt_x>=b:
        return False
    if lb_y>=a:
        return False
    print(lt_y,lt_x, rt_y,rt_x, lb_y,lb_x, rb_y,rb_x)    
    if L[lt_y][lt_x]==L[rt_y][rt_x]:#==L[lb_y][lb_x]==L[rb_y][rb_x]:
        return True
    else:
        return False
    
an=1
for i in range(0,a):
    for k in range(0,b):
        for j in range(1, min(a,b)): #변의 길이
            if i+j>=a or i+j>=b:
                continue
            lt_y=i
            lt_x=k
            
            rt_y=i
            rt_x=k+j
            
            lb_y=i+j
            lb_x=k
            
            rb_y=i+j
            rb_x=k+j    
            
            if is_same(lt_y,lt_x, rt_y,rt_x, lb_y,lb_x, rb_y,rb_x):
                an=max(an,j+1)
print(an**2)