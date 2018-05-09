#!/usr/bin/env python

import glob

find = '.'
replace = ','

for filename in glob.glob('*.txt'):
	f = open(filename, 'r')
	string = f.read()
	f.close()
	replaced = string.replace(find, replace)
	print(replaced)
