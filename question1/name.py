#!/usr/bin/env python

import glob, os

find = '.'
replace = ','

if not os.path.exists('replace'):
	os.mkdir('replace')

for filename in glob.glob('*.txt'):
	with open(filename, 'r') as f:
		string = f.read()	
	replaced = string.replace(find, replace)
	with open('replace/' + filename, 'w') as f:
		f.write(replaced)
	
