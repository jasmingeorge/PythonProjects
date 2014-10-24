from sys import argv

script, filename = argv

print "Erase %r." % filename
print "hit CTRL^C to cancel"
print "hit ENTER to proceed"
raw_input("?")

print "Opening file"
target = open(filename, 'w')

print "Truncate file"
target.truncate()

print "Write 3 lines"
line1 = raw_input("Line 1 : ")
line2 = raw_input("Line 2 : ")
line3 = raw_input("Line 3 : ")

print "going to write these to files"

target.write(line1+"\n"+line2+"\n"+line3+"\n")
print "Close"
target.close()
print "Open %r for reading" % filename

file = open(filename, 'r')
txt = file.read()
print txt
