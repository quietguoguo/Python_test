def fibs(num):
    'fibs writen by GG'
    fibs = [ 0,1 ]
    for i in range(num-2):
        fibs.append(fibs[-2]+fibs[-1])
    return fibs

def hello_you(name):
    return 'Hello ' + name

a=hello_you('GG')
print a

a=fibs(4)
#print a
print fibs.__doc__
help(fibs)