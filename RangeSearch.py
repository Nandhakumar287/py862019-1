L,R,N=map(int,input().split())
n=str(N)
li=[]
c=0
for i in range(L,R+1):
  li.append(str(i))
for j in range(0,len(li)):
  if(n in li[j]):
    c+=1
print(c)    
