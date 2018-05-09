#!/usr/bin/env python

import glob, os, sys

if len(sys.argv) !=  3:
	raise ValueError('replace.py takes 2 arguments') 

find, replace = sys.argv[1:]

if not os.path.exists('replace'):
	os.mkdir('replace')

for filename in glob.glob('*.txt'):
	with open(filename, 'r') as f:
		string = f.read()	
	replaced = string.replace(find, replace)
	if replaced != string:
		with open('replace/' + filename, 'w') as f:
			f.write(replaced)
	
