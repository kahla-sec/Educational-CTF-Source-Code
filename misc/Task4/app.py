from random import randint

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

import sys
sys.stdout = Unbuffered(sys.stdout)

flag="Securinets{g00d_j0b_On_Sav1ng_th3_pl4n3t!}"

class Error(Exception):
	pass

class ZeroError(Error):
	pass

def welcome():
	print ("\nCOVID-19 hit hard our city. Our population is estimated to 10'000. Scientific researchers are working on a treatment but his current efficiency is growing slowly. You should save us from the virus in less than 3 days. Otherwise, we'd all be dead.\n")

def info(day,efficacity,population):
	print ("\nDay                : "+str(day))
	print ("Current population : "+str(population))
	print ("Treatment progress : "+str(efficacity)+"%\n")

def getNumericDay():
	while 1:
		try:
			x = raw_input("Input:")
			x = int(x)
			if x == 0:
				raise ZeroError
			break
		except (ValueError, NameError):
			print "\nplease enter a number.\n"
		except ZeroError:
			print "\nYou can't use your stopwatch\n"
	return x

def getNumericEfficacity():
	while 1:
		try:
			x = raw_input("Input:")
			x = int(x)
			if x>15 or x<1:
				raise ValueError
			break
		except (ValueError, NameError):
			print "\nplease enter a value in [1,15]\n"
	return x

def check(efficacity,population):
	if population<1:
		print("What an apocalypse! The humanity is forever gone!\n")
		exit(0)
	if efficacity>99:
		print("Thanks Doc! Here's your reward:")
		print flag
		exit(0)

def main():
	efficacity=15
	day=0
	population=10000
	welcome()
	while 1:
		check(efficacity,population)
		info(day,efficacity,population)
		print("\nHow much improvement did researchers achieve today towards finding a treatment?\n")
		e = getNumericEfficacity()
		efficacity += e
		print("\nhow many days needed for this improvement?\n")
		d = getNumericDay()
		day += d
		deaths = 0
		while d>0:
			deaths += randint(3334,4200)
			d-=1
		print("\n\nTotal deaths in that period : "+str(deaths)+"\n")
		population -= deaths

if __name__ == '__main__':
	main()

	


