i=int(raw_input('jlr'))
a=[1000000,600000,400000,200000,100000,0]
b=[0.01,0.015,0.03,0.05,0.075,0.1]

p=0
print len(a)
for r in range(0,len(a)):
    print r
    if i > a[r]:
        p+=(i-a[r] )*b[r]
        i=a[r]
print p
        