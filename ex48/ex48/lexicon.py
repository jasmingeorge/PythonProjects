#scan should take a value and return a tuple
def scan(val):
	words = val.split()
	tuples=[]
	for value in words:
		if(value in {"north","south","east","west","down","up","left","right","back"}):
			tuples.append(('direction',value))
		elif(value in {"go","stop","kill","eat"}):
			tuples.append(('verb',value))
		elif(value in {"the","in","of","from","at","it"}):
			tuples.append(('stop',value))
		elif(value in {"door","bear","princess","cabinet"}):
			tuples.append(('noun',value))
		elif(value in {'0','1','2','3','4','5','6','7','8','9'}):
			tuples.append(('number', int(value)))
		else:
			tuples.append(('error',value))
	return tuples
