from napalm import get_network_driver
driver = get_network_driver('ios') # using IOS driver here which may be Junos for Juniper.
Var_device = driver('200.1.1.10', 'cisco', 'cisco') # providing IP, username and password.
Var_device.open() #SCP

ios_output = Var_device.get_facts() #using get_facts function from Napalm lib.
print (ios_output)

#pip install napalm