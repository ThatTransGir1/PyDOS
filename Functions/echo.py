def echo(list1,list2):
    echoList = []
    index = list1.index(list2)
    for i in list1[index+1:]:
        echoList.append(i)
    print(" ".join(echoList))