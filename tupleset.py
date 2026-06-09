tuple1=("sarah","sheba","sharon")
print(tuple1)
print(len(tuple1))
#creating a tuple with only one item
tuple2=("sheila",)
print(tuple2)
print(len(tuple2))
#using a tuple constructor to create a tuple
tuple3=tuple(("cup","flask","plate"))
print(tuple3)
print(type(tuple3))
print(len(tuple3))
#Accessing items in a tuple
print(tuple1[1])
tuplex=("san","sun","run","ran")
y=list(tuplex)
y[1]="son"
tuplex=tuple(y)
print(tuplex)
p=("ban","bag","bat")
a,b,c=p
print(a)
print(b)
print(c)
#looping throug a tuple
for x in p:
    print(x)
#using a while loop
tuple1=(1,2,3,4)
i=0
while i <len(tuple1):
    print(tuple1[i])
    i=i+1
#looping through a tuple.
for i in range(len(tuple1)):
    print(i)
#Using a while loop
tuple3=("sat","set","sut","sun","son")
i=0
while i<len(tuple3):
    print(tuple3[i])
    i=i+1
#Taking a look at sets. adding two sets together
set1={"sun","son","sand","said"}
print(set1)
set2={"cat","cut","can","cant"}
set1.update(set2)
print(set1)
#Adding another item into aset
set2.add("sad")
print(set2)
#Removing an item from a set
set1.remove("said")
print("set1")
set1.discard("cut")
print(set1)
#Looping thru a set
for i in set1:
    print(i)
#union of sets
set4=set1.union(set2)
print(set4)
#frozen sets
x=frozenset({1,2,3,4})
print(x)
print(type(x))
#Dictionary
dict1={
    "age":36,
    "Name":"sarah",
    "height":"167"

}
print(dict1)
print(dict1["Name"])
print(len(dict1))
print(type(dict1))
dict2={
    "name":"sarah",
    "age":36,
    "sex":"Female"
}
print(dict2)
print(dict2["age"])
print(len(dict2))
print(dict2["sex"])
x=dict2["sex"]
print(x)
y=dict2.get("sex")
print(y)
z=dict2.keys()
print(z)
p=dict2.values
print(p)
print(dict2)
dict2["color"]="chocolate"
print(dict2)
dict2.update({"size":32})
print(dict2)
print(dict1)
dict1.update({"school":"kiu"})
dict1["location"]="Bushenyi"
print(dict1)
dict1.pop("location")
print(dict1)
print(dict2)
del dict2["age"]
print(dict2)






