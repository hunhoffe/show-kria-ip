# show-kria-ip

This script displays the local IP address to the grove oled adapter during boot time. In order for it to work properly, make sure you have the necessary setup to connect to a wifi network at boot time (you can do so by using wpa\_supplicant and dhclient [link](https://github.com/Bruteforceman/kria-wifi)).

After you run the script to connect your board to the wifi network at boot time, you need to make the setup.sh script executable by running `sudo chmod +x setup.sh`. After that, you simply run 

```
sudo ./setup.sh
```

Then reboot your board and test if the oled adapter showing the IP properly.
