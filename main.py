alist=[] #empty list
blist=[1,2,3] #elements in list
clist=["a","b","c"] # string elements in list
dlist=[1,2,3,6,1,1,2,2] #List can accept repeated elements
elist=[1,"one",1.5,1+5j,True,[5,6,"aa"],(5,9,"lk"),{1,2,"a"},{1:96,"a":"aa"},range(3)] #List accept all types of elements
print(alist)
print(blist)
print(clist)
print(dlist)
print(elist)
#indexing
print(clist[1])
#mutability
myfavcolors=["red","yellow","orange"]
print("Before updation list elements",myfavcolors)
#myfavcolors[3]=”white” -error because index range is only 2
myfavcolors[2]="white"
print("After updation list elements",myfavcolors)

#Is this possible to mutable list of elements
myfavnumbers=[1,5,7,9,15,21]
#mutability
print("Before updation list elements",myfavnumbers)
myfavnumbers[2]=6
print("After updation list elements",myfavnumbers)
#yes it's possible using frozen set
#frozenset() is an inbuilt function is Python 
#which takes an iterable object as input and makes them immutable
#Syntax : frozenset(iterable_object_name)
#Parameter : This function accepts iterable object as input parameter.
#Return Type: This function return an equivalent frozenset object.
# making it frozenset type 
f_num=frozenset(myfavnumbers)  
# below line will generate error 
f_num[1] = 90
