import win32com.client

if __name__ == '__main__':
    wmi = win32com.client.GetObject("winmgmts:")
    for usb in wmi.InstancesOf("win32_usbcontrollerdevice"):
        print(usb.Dependent)
        # if "VID_05E0&PID_2107" in usb.Dependent:
        #     usbPidVidCorrect = True

# import re
#
# import subprocess
#
# device_re = re.compile("Bus\s+(?P\d+)\s+Device\s+(?P\\d+).+ID\s(?P\w+:\w+)\s(?P.+)$", re.I)
#
# df = subprocess.check_output("lsusb")
#
# devices = []
#
# for i in df.split('\n'):
#
#     if i:
#
#         info = device_re.match(i)
#
#         if info:
#
#             dinfo = info.groupdict()
#
#             dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
#
#             devices.append(dinfo)
# print(devices)
