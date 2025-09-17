# s=input("Enter:")
# v=s.strip()
# l=v.split(" ")
# x={}
# for i in l:
#     if i in x:
#         x[i] += 1
#     else:
#         x[i] = 1
# print(x)

# x="MoHammAdrEza"
# s={"U":0,
#   "L":0}
# for i in x:
#     v=i.isupper()
#     if v==True:
#         s["U"]+=1
#     else:
#         s["L"]+=1
# print(s)

# x="mohammadreza"
# s={}
# for i in x:
#     if i not in s:
#         s[i]=1
#     else:
#         s[i]+=1
# print(s)

grade_student=[
    {"id":1,"M":60,"F":40,"avg":0},
    {"id":2,"M":80,"F":70,"avg":0}
]
for i in grade_student:
    x=(i["M"]+i["F"])/2
    i["avg"]=x
    i.pop("M")
    i.pop("F")
print(grade_student)