#!/usr/bin/python
import test

def hello():
	print "call hello function"

if __name__=="__main__":
	print "In first file"
	hello()
	test.test_func()
