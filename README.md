# show-kria-ip

This script connects to a wifi and displays the IP address, SSID and the password on the grove oled adapter during boot time. The script uses nmcli to connect to the wifi, which is enabled by default in your system. 

First, you need to make the setup.sh script executable by running `sudo chmod +x setup.sh`. After that, you simply run 

```
sudo ./setup.sh
```

Now you need to create a config file to connect to the wifi. Create a new file named `nmcli.json` in the `/etc/` directory
```
sudo touch /etc/nmcli.json
```

Now edit the the file with your favorite editor by `sudo vim /etc/nmcli.json`. Inside this file you need to write configurations for your wifi network, using the following format:
```
[
	{
		"ssid": "ssid-1",
		"password": "pwd1",
		"hidden": 0,
		"priority": 2,
	},
	{
		"ssid": "ssid-2",
		"password": "pwd2",
		"hidden": 1,
		"priority": 100
	}
]
```

Here you can see an example of the nmcli.json file. The file must contain an array of json objects that has these 4 mandatory attributes: `ssid`, `password`, `hidden`, and `priority`. 

In the `ssid` and `password` fields, you will have to write the SSID and the password of your wifi network respectively. `hidden` should be 0 if the network is not hidden and 1 otherwise. In the`priority` field, you can set the priority of the connections. Higher number of means higher priority, so in the example above, the script will try to connect to the wifi network ssid-2 first.


After you've populated nmcli.json file with necessary information, reboot your board and test if the oled adapter showing the IP properly. Your board should be connected to the PMOD Grove Adapter at reboot time and the OLED display should be connected to the G4 port of the GROVE adapter.

## Troubleshooting
1. If you can't see anything on the display, make sure the OLED display is connected to the G4 port in the adapter.
2. If you're getting "No network" on the OLED display, power-cycle the board again. If you still can't connect to the network after a few power-cycling, make sure your nmcli.json file was formatted properly
3. If you can see the wifi network on the OLED display but can't connect to it via ssh/jupyter or ping, power-cycle the board 1-2 times.

