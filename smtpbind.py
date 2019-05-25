#!/usr/bin/python3.5
# smtpbind.py 5/25/2019 dwg - 
# Copyright (C) 2019 Douglas Wade Goodall. All Rights Reserved.

import os
import sys
import smtplib
import credentials

def smtp_send(subject,body):
    try:
        szMsg = "From: "
        szMsg += credentials.SMTPFROM
        szMsg += "\r\nTo: "
        szMsg += credentials.SMTPDEST
        szMsg += "\r\nSubject: " + subject + "\r\n\r\n" + body
        server = smtplib.SMTP_SSL( credentials.SMTPHOST, credentials.SMTPPORT )
        server.login(credentials.SMTPUSER,credentials.SMTPPASS)
        server.set_debuglevel(1)
        server.sendmail(credentials.SMTPFROM, credentials.SMTPDEST, szMsg)
        server.quit()
        return True
    except:
        return False

#####################
# eof - smtpbind.py #
#####################
