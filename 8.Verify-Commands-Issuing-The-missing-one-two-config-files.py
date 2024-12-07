import json
from napalm import get_network_driver
import os
os.chdir(r'C:\Users\Administrator\Desktop\work\PythonWeek3')
driver = get_network_driver('ios')
Var_device = driver('200.1.1.10', 'cisco', 'cisco')
Var_device.open()
print ('Accessing 200.1.1.10')

Var_device.load_merge_candidate(filename='ACL.txt')
Var_diffs = Var_device.compare_config()
if len(Var_diffs) > 0:
    print(Var_diffs)
    Var_device.commit_config()
else:
    print('No ACL changes required.')
    Var_device.discard_config()

Var_device.load_merge_candidate(filename='spanning.txt')
Var_diffs = Var_device.compare_config()
if len(Var_diffs) > 0:
    print(Var_diffs)
    Var_device.commit_config()
else:
    print('No Spanning changes required.')
    Var_device.discard_config()
Var_device.close()

#Question - How we can avoid the code using two times??