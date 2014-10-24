from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(f):
	print f.readline()

current_file = open(input_file)

print "Whole File"

print_all(current_file)

print "Rewind"

rewind(current_file)

print "Let's print three lines."

print_a_line(current_file)

print_a_line(current_file)

rewind(current_file)

print_a_line(current_file)

