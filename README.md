# TasmotaAutoStatus for Tasmota and CraftbeerPi (Raspberry Pi) v0.1
This script forces via an HTTP command the configured Tasmota device to send sensor data over MQTT

## Installation

Download the files via GIT command or browser
```
git clone https://github.com/stamandster/TasmotaAutoStatus
```

Copy both TasmotaAutoStatus.sh and TasmotaAutoStatus.py to /usr/local/sbin and set permissions
```
cd TasmotaAutoStatus
sudo cp TasmotaAutoStatus* /usr/local/sbin/
sudo chmod +x /usr/local/sbin/TasmotaAutoStatus*
```

Change the IP address queried in the script to your individual Tasmota IP, and set your query "sleep" rate (default is 1 second)
```
sudo nano /usr/local/sbin/TasmotaAutoStatus.py
```

Configure Crontab
```
sudo crontab -e
```

Add the following line at the end of the file and save

```
# monitor and start onewireMonitor is process is not running
*/1 * * * * root /usr/local/sbin/TasmotaAutoStatus.sh > /dev/null 2>&1
```

Alternatively, you can run this script from any location manually (for instance your downloads folder) in the user context, just remember to edit the IP and Sleep timer

```
cd Downloads
python TasmotaAutoStatus.py
```
