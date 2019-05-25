#!/usr/bin/python3.5

import sys
import smtpbind

if True == smtpbind.smtp_send("Status message from "+__file__, "This is the body"):
    print("Email send success\n")
    sys.exit(0)
else:
    print("Email send failure\n")
    sys.exit(1)


