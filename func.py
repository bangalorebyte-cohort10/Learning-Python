#!/usr/bin/env python3

def function_addition(arg1,arg2):
	arg1 = 10
	arg2 = 20
	return(arg1+arg2)

def function_list(l, a):
	print('IN function',l,a)
	l[0] = 20
	a = 30

L = [1,2,3,4]
a = 40

function_list(L,a)
print(L)
