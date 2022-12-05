a= input()
a=a.split(' ')
building=int(a[0])
me=int(a[1])
step=int(a[2])
an=0
an+=step//(building-1)
if step%(building-1)!=0:
    an+=1
print(an)