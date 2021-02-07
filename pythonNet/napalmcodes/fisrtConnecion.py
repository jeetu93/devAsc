# connect to single cisco ios  device

import json

from napalm import get_network_driver

driver = get_network_driver("ios")

iosvl2 = driver('172.16.254.60', 'cisco', 'nso123')

iosvl2.open()

# get facts about this device
ios_output = iosvl2.get_facts()

#ios_output = iosvl2.get_interfaces_ip()
#ios_output = iosvl2.get_config(retrieve='all') // need to convert the config \n to newline
#ios_output = iosvl2.get_arp_table() # you can use as well get_arp_table(vrf='') 

# print the json output in pretty format indentation is added for output readability
# print(ios_output)

print(json.dumps(ios_output, indent=4))

#print(json.dumps(ios_output, indent=4,sort_keys=True))

iosvl2.close()


