
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

hostname = "google.com"
# response = os.system("ping -c 1 " + hostname) -> este seria para Windows
response = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")


if response == 0:
    print (hostname + " responde")
else:
    print (hostname + " no responde")
