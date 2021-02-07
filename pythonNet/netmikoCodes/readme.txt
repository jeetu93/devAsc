check first netmiko is installed or not
pip3 show netmiko
else download or install it
pip3 install netmiko

# first error encountered
# later it was fixed by changing the device_type in the python script


root@0a94f6e2e4f7:/var/opt/devNet/devAsc/pythonNet/netmikoCodes# python3 firstNetmikocode.py
Traceback (most recent call last):
  File "firstNetmikocode.py", line 11, in <module>
    net_connect = ConnectHandler(**R1)
  File "/usr/local/lib/python3.6/dist-packages/netmiko/ssh_dispatcher.py", line 312, in ConnectHandler
    "currently supported platforms are: {}".format(msg_str)
ValueError: Unsupported 'device_type' currently supported platforms are:
a10
accedian
adtran_os
alcatel_aos
alcatel_sros
apresia_aeos
arista_eos
aruba_os
aruba_osswitch
aruba_procurve
avaya_ers
avaya_vsp
broadcom_icos
brocade_fastiron
brocade_netiron
brocade_nos
brocade_vdx
brocade_vyos
calix_b6
centec_os
checkpoint_gaia
ciena_saos
cisco_asa
cisco_ftd
cisco_ios
cisco_nxos
cisco_s300
cisco_tp
cisco_wlc
cisco_xe
cisco_xr
cloudgenix_ion
coriant
dell_dnos9
dell_force10
dell_isilon
dell_os10
dell_os6
dell_os9
dell_powerconnect
dlink_ds
eltex
eltex_esr
endace
enterasys
ericsson_ipos
extreme
extreme_ers
extreme_exos
extreme_netiron
extreme_nos
extreme_slx
extreme_vdx
extreme_vsp
extreme_wing
f5_linux
f5_ltm
f5_tmsh
flexvnf
fortinet
generic
generic_termserver
hp_comware
hp_procurve
huawei
huawei_olt
huawei_smartax
huawei_vrpv8
ipinfusion_ocnos
juniper
juniper_junos
juniper_screenos
keymile
keymile_nos
linux
mellanox
mellanox_mlnxos
mikrotik_routeros
mikrotik_switchos
mrv_lx
mrv_optiswitch
netapp_cdot
netgear_prosafe
netscaler
nokia_sros
oneaccess_oneos
ovs_linux
paloalto_panos
pluribus
quanta_mesh
rad_etx
raisecom_roap
ruckus_fastiron
ruijie_os
sixwind_os
sophos_sfos
tplink_jetstream
ubiquiti_edge
ubiquiti_edgerouter
ubiquiti_edgeswitch
ubiquiti_unifiswitch
vyatta_vyos
vyos
watchguard_fireware
yamaha
zte_zxros


# After device_type fix results we got 
root@0a94f6e2e4f7:/var/opt/devNet/devAsc/pythonNet/netmikoCodes# python3 firstNetmikocode.py

Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR

Gateway of last resort is not set

      10.0.0.0/32 is subnetted, 8 subnets
B        10.0.111.111 [200/0] via 172.16.254.68, 3d04h
B        10.0.112.112 [200/0] via 172.16.254.69, 3d08h
C        10.1.2.1 is directly connected, Loopback0
B        10.10.17.1 [200/0] via 172.16.254.68, 3d04h
B        10.10.18.1 [200/0] via 172.16.254.69, 3d08h
B        10.10.170.1 [200/0] via 172.16.254.68, 3d04h
B        10.10.180.1 [200/0] via 172.16.254.69, 3d08h
C        10.20.10.1 is directly connected, Loopback1
      112.0.0.0/32 is subnetted, 1 subnets
C        112.112.112.1 is directly connected, Loopback5
      172.16.0.0/16 is variably subnetted, 3 subnets, 2 masks
S        172.16.253.0/24 [1/0] via 172.16.254.1
C        172.16.254.0/24 is directly connected, GigabitEthernet0/2/7
L        172.16.254.60/32 is directly connected, GigabitEthernet0/2/7
root@0a94f6e2e4f7:/var/opt/devNet/devAsc/pythonNet/netmikoCodes#
