import os
os.chdir(r'C:\Users\Administrator\Desktop\work\PythonWeek3')
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
Var_device = driver('200.1.1.10', 'cisco', 'cisco')
Var_device.open()
print ('Accessing 200.1.1.10')
#SW1(config)#ip scp server enable
Var_device.load_merge_candidate(filename='ACL.txt') #Note: we aren't using any OPEN function here, SCP is doing the job
Var_device.commit_config()
Var_device.close()

print("Configuration is pushed successfully from the file - ACL.txt")