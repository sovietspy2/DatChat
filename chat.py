#!/usr/bin/python
import os
import time
import threading

class LoadingThread(threading.Thread):
	def __init__(self, filename):
		super(LoadingThread,self).__init__()
		self.filename = filename
	def run(self):
		while True:
			if (os.stat(self.filename).st_size!=0):
				f = open(self.filename,'r+')
				for line in f:
					print(line)
				f.seek(0)
				f.truncate()
				f.close()
			else:
				time.sleep(1)

#class AppController():
#	__init__(self):
#		pass

class SendingThread(threading.Thread):
	def __init__(self, filename):
		super(SendingThread,self).__init__()
		self.filename = filename

	def run(self):
		while True:
			f = open(self.filename, "a")
			text = input()
			while (text):
				f.write(text+'\n')
				f.flush()
				text = input()
		

sender = SendingThread("chat2.txt")
reciver = LoadingThread("chat.txt")

sender.run()
reciver.run()