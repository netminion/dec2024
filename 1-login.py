import paramiko
import time
#from getpass import getpass
ip = '200.1.1.10'
username = 'cisco'
password = 'cisco'

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)
DEVICE_ACCESS = SESSION.invoke_shell() #ssh to the device is taken

DEVICE_ACCESS.send(b'term length 0\n') #this is again a BYTE String
DEVICE_ACCESS.send(b'show run\n')
time.sleep(1) #Need to get wait for sometime - here 5 sec as an example

output = DEVICE_ACCESS.recv(65000) #buffer size is 65K which can be lower depending upon data receiving.
print (output.decode('ascii'))
SESSION.close