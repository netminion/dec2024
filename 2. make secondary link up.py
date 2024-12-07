from netmiko import ConnectHandler
#from operator import itemgetter
deviceIP = {
    'device_type':'cisco_ios',
    'ip':'200.1.1.20',
    'username':'cisco',
    'password':'cisco'
}
connect = ConnectHandler(**deviceIP) #SSH to the device through Netmiko
output=connect.send_command('sh ip int br', use_textfsm=True) #This is a way to issue single command, but if there are multiple commands we need to use LISTS
print(output)
#intlen  = (len(output))

print("\nChecking primary Link status - Interface {} status is {}".format(output[1]['intf'],output[1]['status']))

if  output[1]['status']=='up':
    print("\nSince primary link is up, nothing to be change - Thanks and have a good time\n")
else:
    print("\nBringing up secondary link\n")
    cmd=['int eth0/2','no shut']
    output = connect.send_config_set(cmd)
    print(output)
