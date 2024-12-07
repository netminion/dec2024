import paramiko
import time
import datetime
import os
os.chdir(r'C:\Users\Administrator\Desktop\work\PythonWeek3')
TNOW1 = datetime.datetime.now().replace(microsecond=0)
TNOW2 = str(TNOW1).replace(':','_')
TNOW = TNOW2.replace(" ", "_") #date and time to get find.

DEVICE_LIST = open ('device.txt')
for n in DEVICE_LIST:
    IP = n.strip()
    print ('\n #### Connecting to the device ' + IP + '####\n' )
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(IP,port=22,
    username='cisco',
    password='cisco',
    look_for_keys=False,
    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    DEVICE_ACCESS.send(b'terminal len 0\n')
    DEVICE_ACCESS.send(b'show run\n')
    time.sleep(1)
    output = DEVICE_ACCESS.recv(65000)
    print (output.decode('ascii'))
    
    SAVE_FILE = open('DEVICE_' + IP + str(TNOW) + '.txt', 'w') #str(TNOW1) will also works
    SAVE_FILE.write(output.decode('ascii'))
    SAVE_FILE.close

    SESSION.close

print ("\n\nFiles are saved in the asked directory - please check. Have a nice day!\n\n")