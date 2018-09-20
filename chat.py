#!/usr/bin/python
import os
import time

while True:
	
	if (os.stat('chat.txt').st_size!=0):
		f = open('chat.txt','r+')
		for line in f:
			print(line)
		f.seek(0)
		f.truncate()
		f.close()
	else:
		time.sleep(1)

print('succes')