from kv260 import BaseOverlay
from pynq_peripherals import PmodGroveAdapter
import subprocess as sp
import json, os

def get_ip_address():
    ip_addr = sp.getoutput("ifconfig \"$(ifconfig | awk '$1 ~ /^wl/ {print $1}' | rev | cut -c 2- | rev)\" | grep 'inet ' | cut -f1 | awk '{ print $2 }'")
    return ip_addr

def get_oled():
    base = BaseOverlay('base.bit')
    adapter = PmodGroveAdapter(base.PMODA, G4='grove_oled')
    return adapter.G4

ip_addr = 'localhost'
try:
    ip_addr = get_ip_address()
    print("IP addr is: " + ip_addr)
except:
    print("Get IP Addr failed")
    pass


try:
    oled = get_oled()
    oled.set_default_config()
    oled.set_normal_display()
    oled.deactivate_scroll()
    oled.set_next_row_wrap_mode()

    oled.put_string('{}'.format(ip_addr))
    del oled
except:
    print('No device found')
    
