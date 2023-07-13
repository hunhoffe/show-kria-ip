from kv260 import BaseOverlay
from pynq_peripherals import PmodGroveAdapter
import socket
import time

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip_addr = s.getsockname()[0]
    s.close()
    return ip_addr

def get_oled():
    base = BaseOverlay('base.bit')
    adapter = PmodGroveAdapter(base.PMODA, G3='grove_oled')
    return adapter.G3

try:
    ip_addr = get_ip_address()
except:
    ip_addr = "No IP found"
    
try:
    oled = get_oled()
    oled.set_default_config()
    oled.set_normal_display()
    oled.clear_display()
    oled.put_string(str(ip_addr))
    del oled
except:
    print('No device found')
    
