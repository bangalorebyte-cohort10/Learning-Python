#!/usr/bin/env python3

if __name__ == '__main__':
	listofnumbers = input('Enter the comma separated values ')
	listofstring = listofnumbers.split(',')
	print(listofstring)
	l = [int(listofstring[i]) for i in range(0,len(listofstring))]
	print(l)
	print(tuple(l))