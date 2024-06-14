#!/bin/sh

ps auxw | grep TasmotaAutoStatus.py | grep -v grep > /dev/null
result=$?
echo "exit code: ${result}"
if [ ${result} -eq "0"]; then
   echo "Tasmota AutoStatus running, nothing to do"
else
   echo "Starting Tasmota AutoStatus"
   nohup /usr/bin/python3 /usr/local/sbin/TasmotaAutoStatus.py > /dev/null 2>&1 &
fi
