#!usr/bin/python3
from __future__ import division
import unittest
import requests
import json


n1 = [5,7.1,18/3,5/5,7.885]
n2 = [7,8.67,8/23,6/6,7.511]

add_from_script = []
add_from_test = []
sub_from_script = []
sub_from_test = []
mul_from_script = []
mul_from_test = []


for i in range(0,len(n1)):

	PARAM={"A":Fraction(n1[i]),"B":Fraction(n2[i])}
	
	test_add = n1[i] + n2[i]
	add_from_test.append(round(test_add,3))

	test_sub = n1[i] - n2[i]
	sub_from_test.append(round(test_sub,3))

	test_mul = n1[i] * n2[i]
	mul_from_test.append(round(test_mul,3))


	url_add = 'http://127.0.0.1:5000/add'
	r1 = requests.get(url_add, params=PARAM)
	data1 = r1.json()
	add_from_script.append(round(data1,3))

	url_sub = 'http://127.0.0.1:5000/sub'
	r2 = requests.get(url_sub, params=PARAM)
	data2 = r2.json()
	sub_from_script.append(round(data2,3))

	url_mul = 'http://127.0.0.1:5000/mul'
	r3 = requests.get(url_mul, params=PARAM)
	data3 = r3.json()
	mul_from_script.append(round(data3,3))


	if add_from_script[i] == add_from_test[i]:
		print "Tested addition successfully:OK"
	else:
		print "Failed addition Test"

	if sub_from_script[i] == sub_from_test[i]:
		print "Tested subtraction successfully:OK"
	else:
		print "Failed subtraction Test"

	if mul_from_script[i] == mul_from_test[i]:
		print "Tested multiplication successfully:OK"
	else:
		print "Failed multiplication Test"



