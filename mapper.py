from sys import *
#I appreciate the Rick Roll

#Main function
def main():
	s = "Never gonna give you up never gonna let you down never gonna run around and desert you"
	tally(s)

#Function that tallies up all unique words and counts the duplicates
def tally(string):
	lowerstring = string.lower().split()
	res = {}
	for item in lowerstring:
		if item in res:
			res[item] += 1
		else:
			res[item] = 1
	print(res)

if __name__== "__main__":
	main()