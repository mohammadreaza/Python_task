
x={"n":4,'v':3,'a':1}
import operator
v=operator.itemgetter(1)
print(sorted(x.items(),key=v))