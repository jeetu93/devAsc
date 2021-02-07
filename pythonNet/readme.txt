[ios]
		cisco-ios
		10.10.12.1
cisco/nso123	hostname	127.0.0.1
ssh worked	BGL_KTK_1AC_CASR920R01	172.16.254.60
	BGL_CASR920-3-LNS-2	172.16.254.61
	CHN_CASR920_2	172.16.254.71
	CHN_CASR903-3-LNS-2	172.16.254.74
	CHN_CASR920_1	172.16.254.92


[iosxr]
cisconso/nso123	BGL_BFD_901_1AG_CASR9KTR072	172.16.254.72
RSA key fingerprint	BGL_ASR9K-MPL-1-TEST14	172.16.254.73
	BGL_CASR9K112_3	172.16.254.75
		172.16.254.99


[rfs]
172.16.254.85

[cfs]
172.16.254.80

[bpa]
172.16.254.88 / 91 can be others too

# IMPORTANT
# Keep all devices backup in storeData dir from ansible genie netmiko napalm
# or choose indivisual datastore per network library

