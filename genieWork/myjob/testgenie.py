from genie.conf import Genie

testbed = Genie.init("testbed.yml")

for device in testbed.devices:
    print(device) ## it will print all devices name mentioned in testbed file
    #testbed.devices[device].connect()
    #interfaceDetail = testbed.devices[device].parse("show interfaces")
    #device_int_details[device.hostname:interfaceDetails]
