#--coding=utf8--
print "hello world"
def logger(func):
    print '现在时间:不知道'
 
    return func
@logger 
def a():
    print 'zenme?'

a()
a()