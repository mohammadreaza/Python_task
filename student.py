student=[
    {"id":123  ,"name":"ali"  ,"ispassed":True  ,"grade":18},
    {"id":378 ,"name":"taha" ,"ispassed":False  ,"grade":5},
    {"id":934 ,"name":"sara" ,"ispassed":True  ,"grade":20},
    {"id":378 ,"name":"reza" ,"ispassed":False  ,"grade":5},
    {"id":377 ,"name":"mahan" ,"ispassed":True  ,"grade":20}
]
count=0
namee=0
less=0
more=0
x=input("Enter your name:")
name1=[]
name2=[]
for i in (student):
    count+=1
    if i["name"]==x:
        namee+=1
    if i["grade"]<10:
        name1.append(i["name"])
        less+=1
    if i["grade"]>10:
        name2.append(i["name"])
        more+=1
print(f"more than ten:{more,name2},less than ten:{less,name1},name student:{namee},count:{count}")
    