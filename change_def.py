def change_def(n):
    n='Mr n'
    print n
    return 'in'
name='Mr name'
w=change_def(name)
print w
print 'out '+name


def change_list(n):
    a=n[:]

    a[0]='Mr N'

name=['Mr W','Mr X']
change_list(name)
print name


a=['a','b','c','d','e','f']
b=a[0::1]
print a is b
print a == b
a[0]='c'
print a is b
print a[:]
print b