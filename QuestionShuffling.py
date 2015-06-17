import numpy as np
# import text file, which has a determined format
a=open("test.dat")
b=open("test2.dat","w")
f=a.read()
g=f.split("\n")
q1=[g[11*i:11*(i+1)] for i in range(30)]
# these two lines can be commented if you want to shuffle last question also
last=q1[-1]
q2=q1[:-1]
np.random.shuffle(q2)

for q in q2: 
	alts=q[4:9]
	np.random.shuffle(alts)
	q=np.concatenate([q[:4],alts,q[-2:]])
	for l in q:
		b.write(str(l)+"\n")
# comment this block also if you want to shuffle last question
alts=last[4:9]
np.random.shuffle(alts)
last=np.concatenate([last[:4],alts,last[-2:]])
for l in last:
	b.write(str(l)+"\n")		

a.close()
b.close()
