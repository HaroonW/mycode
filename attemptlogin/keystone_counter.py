#!/usr/bin/python3
loginfail = 0
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
keystone_file_lines=keystone_file.readlines()
for i in keystone_file_lines:
    if "- - - - -] Authorization failed" in i:
        loginfail += 1
print("the number of failed login attempt is " + str(loginfail))
