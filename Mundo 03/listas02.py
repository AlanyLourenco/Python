test=[]
test.append('Alany')
test.append(19)
list2=[]
list2.append(test[:])
test[0]='Maria'
test[1]=22
list2.append(test[:])
print(list2)