from sys import argv

script, filename = argv

txt = open(filename)

print "file %r" %filename
print txt.read()
