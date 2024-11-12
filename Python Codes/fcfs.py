n=int(input("Enter the number of Processes:"))
d={}
l=[]

for i in range(n):
    pid=input("Enter process id here:")
    l.append(pid)

    keys=int(input(f"Enter the arrivial time of {pid}: "))
    values=int(input(f"Enter the burst time of {pid}: "))
    d.update({keys:values})

print(d)
print(l)

dk=list(d.keys())
dk.sort()
sdk={i:d[i] for i in dk}
print(sdk)

dv=list(sdk.values()) 
print(dv)

et=[]
st=0
for i in range(n):
    st=st+dv[i]
    et.append(st)

print(et)

tat=[]
for i in range(n):
    t=et[i]-dk[i]
    tat.append(t)
print(tat)

wt=[]
for i in range(n):
    w=tat[i]-dv[i]
    wt.append(w)
print(wt)

avg_tat=sum(tat)/n
avg_wt=sum(wt)/n

print(f"The average Turn around time is: {avg_tat}\nThe average waiting time is: {avg_wt}")