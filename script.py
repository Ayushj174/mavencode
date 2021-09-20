#import requests
import json
import sys
import time
import subprocess
import os
#result = subprocess.run(['ls'], stdout=subprocess.PIPE)
#var = result.stdout.decode('utf-8')
#print(var)
#output = os.popen ("date").read()
#print (output)
getVersion =  subprocess.Popen("git diff HEAD HEAD~ --name-only | cut -d '/' -f2 | uniq", shell=True, stdout=subprocess.PIPE).stdout
version =  getVersion.read()
p1 = version.decode()
p2 = p1.strip()

print( p2)
