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
#print(output)
#print("\n",output[5])#['status '])
intlen  = (len(output)) #5

'''output valus is a list = [{'intf': 'Ethernet0/0', 'ipaddr': '200.1.1.20', 'status': 'up', 'proto': 'up'}, {'intf': 'Ethernet0/1', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'}, {'intf': 'Ethernet0/2', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'Ethernet0/3', 'ipaddr': 'unassigned', 'status': 'up', 'proto': 'up'}, {'intf': 'Loopback11', 'ipaddr': '11.1.1.1', 'status': 'up', 'proto': 'up'}, {'intf': 'Loopback12', 'ipaddr': '12.1.1.1', 'status': 'up', 'proto': 'up'}, {'intf': 'Vlan1', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'}]'''
ip = "11.1.1.1" #user input

intf = [n['intf'] for n in output if n['ipaddr']==ip ] #using list comprehension

if len(intf)!=0:
    print("{} IP belongs to the interface - {}".format(ip,intf[0]))
else:
    print("Sorry this IP {} does not exits".format(ip))