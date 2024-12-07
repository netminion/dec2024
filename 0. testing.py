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
print(output)

'''vrf = "netminion"
ip = "1.1.1.1"
print("ping {} vrf {}".format(vrf,ip))

a = [n for n in range(2,20)]
print(a)

b = [n for n in range(2,20) if n%2==0]
print(b)'''