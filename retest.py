import re
print 'readlines'
file=open("/etc/hosts")
for line in file.readlines():
    if re.search("^#|^::",line):
        pass
    else:
        print line
file.close()


print 'readline'
file=open("/etc/hosts")
line=file.readline()

while (line):
    if re.search("^#|^::",line):
        line=file.readline()
        continue
    else:
        print line
    line=file.readline()