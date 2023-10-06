def chngtitle(list1,list2):
	list = []
	index = list1.index(list2)
	for i in list1[index+1:]:
		list.append(i)
	msg = " ".join(list)
	drivercode = "\x1B]0;%s\x07"
	print(drivercode % msg)
def termtitle(string):
	drivercode = "\x1B]0;%s\x07"
	print(drivercode % string)
