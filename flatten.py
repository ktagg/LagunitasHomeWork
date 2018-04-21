from sys import *


#Main Function
def main():
	objects = [[1,2],3,[[4,5],6],7]
	runner(objects)

#Function that prints out the result of the recursive function
def runner(input):
	print(sorted(flattener(input)))

#Recursive function to handle the lists
def flattener(input):
	if input == []:
		return input
	if isinstance(input[0], list):
		return flattener(input[0]) + flattener(input[1:])
	return input[:1] + flattener(input[1:])
	
if __name__== "__main__":
	main()