import signal
import urllib.request
import time
import os
import datetime

#handle kill signal 1
def handle_exit(sig, frame):
   raise(SystemExit)
#handle kill signal 2
def setup_OSsignal():
   signal.signal(signal.SIGTERM, handle_exit)

setup_OSsignal()

print("\n\n{} - Starting Tasmota Auto Status".format(datetime.datetime.now()))

try:
   print("{} - ... Running".format(datetime.datetime.now()))
   while True:
      #print("{} - Tasmota Auto Status Cycle".format(datetime.datetime.now()))
      contents = urllib.request.urlopen("http://192.168.1.50/cm?cmnd=status%208").read()
      time.sleep(1)

except KeyboardInterrupt:
   print("")

except SystemExit:
   print("")

except:
   print("")

finally:
   print("{} - Exiting Tasmota Auto Status".format(datetime.datetime.now()))
