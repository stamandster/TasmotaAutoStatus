# TasmotaAutoStatus for Tasmota and CraftbeerPi (Raspberry Pi) v0.1
This script forces via an HTTP command the configured Tasmota device to send sensor data over MQTT

## Installation

- Download the files via GIT command or browser
-     git clone https://github.com/stamandster/TasmotaAutoStatus
- Copy both TasmotaAutoStatus.sh and TasmotaAutoStatus.py to /usr/local/sbin and set permissions
-     cd TasmotaAutoStatus
-     cp TasmotaAutoStatus* /usr/local/sbin/
-     chmod +x /usr/local/sbin/TasmotaAutoStatus*
- Find out the folder / DS18B20 serial to monitor
- Change the IP address queried in the script to your individual Tasmota IP, and set your query "sleep" rate (default is 1 second)
-     nano /usr/local/sbin/TasmotaAutoStatus.py
- Configure /etc/crontab and add the following line at the end of the file
-     nano /etc/crontab
  
      ```
      # monitor and start onewireMonitor is process is not running
      */1 * * * * root /usr/local/sbin/TasmotaAutoStatus.sh > /dev/null 2>&1
      ```
