def hello_world():
	'''"hello_world()" will take no arguments and 
	will return the string "Hello World!" 
	exactly as shown.'''
	return "Hello World!"

def hello_world_n(N):
	'''"hello_world_n(N)" will take one argument (N) and 
	will return the string "Hello World! Hello World! 
	Hello World! ... Hello World!" with exactly N repetitions.'''
	TMP = "Hello World! "
	return TMP*N[:-1]
