# connect to single cisco ios  device
from napalm import get_network_driver

driver = get_network_driver("ios")

iosvl2 = driver('172.16.254.60', 'cisco', 'nso123')

iosvl2.open()

# get facts about this device
ios_output = iosvl2.get_facts()

print (ios_output)

iosvl2.close()


