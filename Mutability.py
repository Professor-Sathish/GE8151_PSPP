#mutability
myfavcolors=["red","yellow","orange"]
print("Before updation list elements",myfavcolors)
#myfavcolors[3]=”white” -error because index range is only 2
myfavcolors[2]="white"
print("After updation list elements",myfavcolors)

#Immutable
#Is this possible to Immutable list of elements
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