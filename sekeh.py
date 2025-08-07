import random
x=["back","front","back","back"]
d={"back":0,"front":0,}
n=100
for i in range(n):
    v=random.choice(x)
    d[v]+=1
print(d)

