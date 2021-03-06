#!/usr/bin/env python

import random
import string
import calendar
import time
import sys
import stomp

NUM_MESSAGES=1000000

conn = stomp.Connection10([('ugster11.student.cs.uwaterloo.ca','61613')])
 
conn.start()
 
conn.connect()
 
messages = []

times = []

msg = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))

for msgId in range(NUM_MESSAGES):
	conn.send('SampleQueue', msg)

	currTime = int(round(time.time() * 1000))
	times.append([msgId, currTime])
	#print ("SENT", body)

# Write the current time every time we send a message
f = open('send.log', 'w')
print('Sent ' + str(len(times)) + ' messages')
for item in times:

#	f.write("%s\n" % item)
	msgId = item[0]
	sendTime = item[1] 
	f.write(str(msgId))
	f.write(" ")
	f.write(str(sendTime))
	f.write("\n")

conn.disconnect()
