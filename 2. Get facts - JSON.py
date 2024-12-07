import json
from napalm import get_network_driver
driver = get_network_driver('ios')
Var_device = driver('200.1.1.10', 'cisco', 'cisco')
Var_device.open()
ios_output = Var_device.get_facts()
print (json.dumps(ios_output, indent=2))
Var_device.close()