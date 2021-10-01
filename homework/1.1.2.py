"""
#1.1.1

N=map(int, input().split())
mass= []
for i in N:
    mass.append(i)
mass.reverse()
print(mass)

#1.1.2
N=map(int, input().split())
mr=True
minn=maxx=0
for i in N:
    if mr:
        minn = maxx =i
        mr=False
    else:
        if i >maxx:
            maxx=i
        if i<minn:
            minn=i
print(maxx,', ', minn)
"""
#1.1.3
N=list(map(int, input().split()))
if len(N)>=5:
    print(mass[2],mass[4])
else:
    for i in range(len(N)-2,-1,-2):
        print(N[i])

"""   

#1.1.4
N=map(int, input().split())
otr=bol=chet=0
for i in N:
    if i%2==0:
        chet+=1
    if i>8:
        bol+=1
    if i<0:
        otr+=1
print(otr, " ", bol, " ", chet)

"""
 
#1.2.1
N=int(input())
och=zaoch=0
    
for i in range(N):
    N=input().split()
    
    for j in N:
        if j == 'True':
            och+=1
        elif j =='False':
            zaoch+=1
            
print(och, " ", zaoch)  
"""
#1.2.3

N=input()
n1=n2=n3=0
c=''
for i in range(len(N)):
    if 64<=ord(N[i])<=90:
        n1=i;break
for i in range(n1, len(N)):
    if 48<=ord(N[i])<=57:
        n2=i;break
for i in range(n2,len(N)):
    if ord(N[i])==46:
        n3=i;break
print(n1,n2,n3)

b=n20n1
for i in range(n1,n3+1,b+1):
    c+=N[i]
print(c)
"""
