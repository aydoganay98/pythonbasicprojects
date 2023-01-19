lis = [['a','b','d'], [3, 4], ['cat', 'mouse', 2]]

for i in range(len(lis)):
    lis[i]=lis[i][::-1]
lis.reverse()
print(lis)