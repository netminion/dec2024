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
#print("\n",output[5])#['status '])
#intlen  = (len(output))

print("\nList of interfaces which are up - ")

#using list comprehension
upintf = ([n['intf'] for n in output if n['status']=='up' ])

a=1
for n in upintf:
    print(str(a)+". "+n)
    a+=1

#for n in range(0,intlen):
#   if output[n]['status']=='up':
#        print(output[n]['intf'] + " status is " + output[n]['status'])

print("\nList of interfaces which are down - ")
print([n['intf'] for n in output if n['status']!='up' ])