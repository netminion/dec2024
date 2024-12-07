import json
from napalm import get_network_driver
import os
os.chdir(r'C:\Users\Administrator\Desktop\work\PythonWeek3')
Dic_devices = ['200.1.1.10', '200.1.1.20']
#SW2(config)#ip scp server enable

def auditing(file_name):
    Var_device.load_merge_candidate(filename=file_name)
    Var_diffs = Var_device.compare_config()
    if len(Var_diffs) > 0:
        print(Var_diffs)
        Var_device.commit_config()
    else:
        print('No ACL changes required.')
        Var_device.discard_config()
for Var_iterate in Dic_devices:
    print ("\nAccessing device with IP - " + str(Var_iterate))
    driver = get_network_driver('ios')
    Var_device = driver(Var_iterate, 'cisco', 'cisco')
    Var_device.open()
    print("\nChecking the ACL configuration mismatch")
    auditing('ACL.txt')
    print("\nChecking the STP configuration mismatch")
    auditing('spanning.txt')
    Var_device.close()