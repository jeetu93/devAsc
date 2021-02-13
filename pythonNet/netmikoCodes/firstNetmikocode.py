from netmiko import ConnectHandler

R1 = {
        'device_type': 'cisco_ios',
        'ip': '172.16.254.60',
        'username': 'cisco',
        'password': 'nso123'
}


net_connect = ConnectHandler(**R1)

output = net_connect.send_command("show ip route")
print (output)
