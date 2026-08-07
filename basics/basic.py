x = {'a' : 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

import copy
x = {'a': [1, 2]}
shallow = x.copy()
deep = copy.deepcopy(x)

x['a'].append(99)
print(shallow)
print(deep)

a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)
print(type(a))
b = {2, 3, 6, 7}
print(a-b)
print(b-a)

my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)