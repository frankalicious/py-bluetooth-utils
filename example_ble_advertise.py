"""
Simple BLE advertisement example
"""
from time import sleep
import bluetooth._bluetooth as bluez

from bluetooth_utils import (toggle_device, start_le_advertising,
                             stop_le_advertising)
#from bluetooth_utils.py
# Advertisement event types
ADV_IND = 0x00
ADV_DIRECT_IND = 0x01
ADV_SCAN_IND = 0x02
ADV_NONCONN_IND = 0x03
ADV_SCAN_RSP = 0x04

dev_id = 0  # the bluetooth device is hci0
toggle_device(dev_id, True)

try:
    sock = bluez.hci_open_dev(dev_id)
except:
    print("Cannot open bluetooth device %i" % dev_id)
    raise

for _ in range(0, 10):
    start_le_advertising(sock,
                         min_interval=2000, max_interval=2000,adv_type=ADV_DIRECT_IND,
                         data=(0x07, 0x00) + (0,) * 29)
    sleep(0.1)
for _ in range(0, 10):
    start_le_advertising(sock,
                         min_interval=2000, max_interval=2000,adv_type=ADV_IND,
                         data=(0x02, 0x01, 0x05, 0x03, 0xff, 0x00, 0x01, 0x06, 0x08, 0x4d, 0x49, 0x20, 0x52, 0x43, 0x03, 0x02, 0x12, 0x18, 0x04, 0x0d, 0x04, 0x05, 0x00, 0x02, 0x0a, 0x00)+ (0,) * 5)
    sleep(0.1)

sleep(3)
stop_le_advertising(sock)


