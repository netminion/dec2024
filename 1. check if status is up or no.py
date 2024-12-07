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
#print("\n",output[4])#['status '])
intlen  = (len(output))
#print(intlen)

#name = output[1]['intf']
#status = output[1]['status']
#print("\ninterface "+ name + " status is " + status)

#print("\ntotal interfaces are ",intlen)

#interface0 = output[1]
#getintf=itemgetter('intf')
#getstatus = itemgetter('status')
#name = getintf(interface0)
#status = getstatus(interface0)
#print("\ninterface "+ name + " status is " + status)

print("\nList of interfaces which are up - \n")
for n in range(0,intlen):
    if output[n]['status']=='up':
        print(output[n]['intf'] + " status is " + output[n]['status'])

print("\nList of interfaces which are down - ")
for n in range(0,intlen):
    if output[n]['status']!='up':
        print(output[n]['intf'] + " status is " + output[n]['status'])