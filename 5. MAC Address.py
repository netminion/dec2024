import json
from napalm import get_network_driver
driver = get_network_driver('ios')
Var_SW = driver('200.1.1.10', 'cisco', 'cisco')
Var_SW.open()
ios_output = Var_SW.get_mac_address_table()
print (json.dumps(ios_output, sort_keys=True, indent=4))
Var_SW.close()