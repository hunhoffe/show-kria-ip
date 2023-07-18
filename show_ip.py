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

def connect_to_network():
    connections = os.listdir('/etc/NetworkManager/system-connections')
    tries = 3

    for file in connections:
        name = file.split('.')[0]
        process = sp.run(['nmcli', 'connection', 'delete', name])
        print('deleted', name, 'with return code', process.returncode)
    
    with open('/etc/nmcli.json', 'r') as f:
        wifis = sorted(json.load(f), key=lambda info: info["priority"], reverse=True)
        sp.run(['nmcli', 'networking', 'on'])
        while sp.run(['nmcli', 'connection', 'show']).returncode != 0:
            pass
        for _ in range(tries):
            for wifi in wifis:
                ssid = wifi["ssid"]
                password = wifi["password"]
                is_hidden = 'yes' if wifi["hidden"] == 1 else 'no'
                process = sp.run(['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', password, 'hidden', 'yes'], capture_output=True)
                if process.returncode == 0:
                    return ssid, password
    return None


ssid, password = 'no network', ''
error = ''
ip_addr = 'localhost'

try:
    creds = connect_to_network()
    ip_addr = get_ip_address()
    if creds is not None:
        ssid, password = creds
except:
    pass


try:
    oled = get_oled()
    oled.set_default_config()
    oled.set_normal_display()
    oled.deactivate_scroll()
    oled.set_next_row_wrap_mode()

    oled.put_string('{}'.format(ip_addr))

    oled.set_position(3, 0)
    oled.put_string('{}'.format(ssid))
    
    oled.set_position(5, 0)
    oled.put_string('{}'.format(password))
    del oled
except:
    print('No device found')
    
