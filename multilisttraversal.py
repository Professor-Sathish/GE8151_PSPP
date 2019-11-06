import itertools 
rollnumbers=["IT01","IT02","IT03","IT04"]
names=["ambika","bhuvana","kavya"]
dept=["ece","it","cse"]
for rnum,name in zip(rollnumbers,names):
	print(rnum,name)
print("==============longest====================")
for (rnum,name,dep) in itertools.zip_longest(rollnumbers,names,dept):
	print(rnum,name,dep)