#!/usr/bin/python3.5

import os
import sys
import smtplib

import credentials

szMsg = "From: "
szMsg += credentials.SMTPFROM
szMsg += "\r\nTo: "
szMsg += credentials.SMTPDEST
szMsg += "\r\nSubject: my auto test msg\r\n"

server = smtplib.SMTP_SSL( credentials.SMTPHOST, credentials.SMTPPORT )
server.login(credentials.SMTPUSER,credentials.SMTPPASS)
server.set_debuglevel(1)
server.sendmail(credentials.SMTPFROM, credentials.SMTPDEST, szMsg)
server.quit()
print("Message Sent!!\n")
