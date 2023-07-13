#!/usr/bin/bash

sudo cp show_ip.py /usr/bin/show_ip.py
sudo cp show_ip.sh /usr/bin/show_ip.sh
sudo chmod +x /usr/bin/show_ip.sh
sudo cp show_ip.service /etc/systemd/system/show_ip.service
sudo systemctl enable show_ip.service
