#!/usr/bin/env python
import argparse
import fileinput
import sys
import re
import os, signal

def get_args():
    parser = argparse.ArgumentParser(
        description='Deletes the domain from the firefox HTST list')
    parser.add_argument(
        '-d', '--domain', type=str, help='Domain to delete', required=True)
    args = parser.parse_args() 
    domain = args.domain
    return domain
domain = get_args()

print "\n" 
print "*****    This script was created by      *****"
print "     ____.                ___________.__     "
print "    |    |  ____  _______ \_   _____/|  |    "
print "    |    | /  _ \ \_  __ \ |    __)_ |  |    " 
print "/\__|    |(  <_> ) |  | \/ |        \|  |_ _ "
print "\________| \____/  |__|   /_______  /|_____/ "
print "                                  \/         " 

print "\n[+} Let's kill Firefox process"
for line in os.popen("ps ax | grep firefox | grep -v grep"):
    fields = line.split()
    pid = fields[0]
    os.kill(int(pid), signal.SIGKILL)

user = os.getlogin()
print "\nDomain name to be erased: [ %s ]\n" % domain
fn = "/Users/%s/Library/Application Support/Firefox/Profiles/c4wydihh.default/SiteSecurityServiceState2.txt" % user
f = open(fn, "r")
lines = f.readlines()
found = False
f.close()
for line in lines:
    if re.match(domain, line):
        found = True
        print "[+] %s was found" % domain
        print "[+] %s is going to be deleted" % domain
        f = open(fn, "w")
        for line in lines:
            if not re.match(domain, line):
                f.write(line)
        f.close()
if found == False:
    print "[-] %s was not found, please check if the domain name is correct (www.domain.com)\n"
else:
    print "[+] %s was deleted\n" % domain
