# def c(x):
#     v={}
#     d=x.strip()
#     l=d.split(" ")
#     for i in l:
#         if i in v:
#             v[i]+=1
#         else:
#             v[i]=1
#     print(v)
# c("python created by rossum and hamed hamed hamed")    

# def f(x):
#     v={"U":0,"L":0}
#     for i in x:
#         b=i.isupper()
#         if b:
#             v["U"]+=1
#         else:
#             v["L"]+=1
#     print(v)
# f("MohaMmAdReZa")

# def f(x):
#     s={}
#     for i in x:
#         if i in s:
#             s[i]+=1
#         else:
#             s[i]=1
#     print(s)
# f("mohammadreza")

def grade_student(x):
    for i in x:
        s=(i["F"]+i["M"])/2
        i["avg"]=s
        i.pop("M")
        i.pop("F")
    print(x)
grade_student([{"id":1,"M":60,"F":40,"avg":0},
    {"id":2,"M":80,"F":70,"avg":0}])
