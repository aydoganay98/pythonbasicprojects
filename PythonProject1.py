my_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flat_list = []

def flattenlis(a):
    for i in a:
        if isinstance(i,list):
            flattenlis(i)
        else:
            flat_list.append(i)

flattenlis(my_list)
print(flat_list)

