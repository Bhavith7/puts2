#!usr/bin/python3
import unittest
import requests
import json
from fractions import Fraction

n1 = [5,7.1,18/3,5/5,7.885]
n2 = [7,8.67,8/23,6/6,7.511]

sub_from_script = []
sub_from_test = []


for i in range(len(n1)):

	PARAM={"A":Fraction(n1[i]),"B":Fraction(n2[i])}
	
	test_sub = n1[i] - n2[i]
	sub_from_test.append(round(test_sub,3))

	url_sub = 'http://127.0.0.1:5000/sub'
	r = requests.get(url_sub, params=PARAM)
	data = r.json()
	sub_from_script.append(round(data,3))

	if sub_from_script[i] == sub_from_test[i]:
		print "Tested successfully:OK"
	else:
		print "Failed Test"


