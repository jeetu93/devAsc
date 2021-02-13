root@0a94f6e2e4f7:/var/opt/devNet/devAsc/pythonNet/napalmcodes# python3 fisrtConnecion.py
Traceback (most recent call last):
  File "fisrtConnecion.py", line 2, in <module>
    from napalm import get_network_driver
ModuleNotFoundError: No module named 'napalm'


# now your should install napalm to avoid this issue

pip3 install napalm
pip3 install netmiko
pip3 show netmiko
