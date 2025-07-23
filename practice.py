"""
Your module description
"""
the_list = ['a', 'b', 'c']
counter = 0

for ix in range(len(the_list)):
    print(the_list[ix], end=' ')
    the_list[ix] = counter
    counter += 1
for ix in range(len(the_list)):
    print(the_list[ix], end=' ')
    

print(the_list)