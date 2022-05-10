import random
import string

def getRandString( lenght: int = 10 ) -> str:
	letters = string.ascii_letters + string.digits
	return "".join( [random.choice( letters ) for i in range( 1, lenght+1 )] )