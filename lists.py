List1=["mango","pawpaw","pineapple"]
print(List1)
print(len(List1))
#List constructor
List2=list(("apple","pawpaw","ovacado"))
print(List2)
#Accessing list items.
print(List1[0])
print(List2[1])
#Range of indexes
List3=["rat","cat","dog","person","tree","phone","house"]
print(List3[0:5])
print(List3[:3])
print(List3[3:])
print(List3[:4])
#Changing the value of an item in a list.
ThisList=list(("pan","can","Wan","Man","Tap","cat"))
print(ThisList)
ThisList[2]="ban"
print(ThisList)
#adding an item to the List
HerList=["sarah","stella","sharon"]
HerList.append("sheeba")
print(HerList)
#Inserting an item at a certain position in a list
Fruits=["orange","pineapple","strawberry","pawpaw"]
Fruits.insert(2,"Pine")
print(Fruits)
HerList.extend(Fruits)
print(HerList)
HerList.remove("strawberry")
print(HerList)
HerList.pop(1)
print(HerList)
for x in List1:
    print(x)
print(List1)
for i in range(len(List1)):
    print(List1[i])
    #making a list out of another list using a for loop
Home=["chair","Table","mat","cat","cup"]
Cs=[]
for x in Home:
    if "c" in x:
        Cs.append(x)
print(Cs)
#Making a list out of another list using comprehensive list
Newlist=[x for x in Home if "c" in x]
print(Newlist)
#sorting a list in ascending order.
age=[23,32,20,19,40,30]
age.sort()
print(age)
#Decending order.
age.sort(reverse=True)
print(age)
#try sorting words
names=["ban","apple","cat","rat","mat"]
names.sort()
print(names)
names.sort(reverse=True)
print(names)
#copying a list
count=[2,3,4]
count2=list(count)
print(count2)
print(count)
