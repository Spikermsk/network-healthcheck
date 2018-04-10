#!/usr/bin/env python
from getpass import getpass
import requests
import json
# from .classes import AccessPoint

# key = getpass("Enter API key:")

# sandbox API key

headers = {"X-Cisco-Meraki-API-Key" : key,
           'Content-type': 'Application/json',
           'Accept': 'Application/json'}
#
# org = requests.request(method="GET",
#                        url="https://api.meraki.com/api/v0/organizations",
#                        headers=headers)
# #
#
networks = requests.request(method="GET",
                            url="https://api.meraki.com/api/v0/organizations/549236/networks",
                            headers=headers)

print(json.dumps(networks.json()))
# #
# #
# devices = requests.request(method="GET",
#                             url="https://api.meraki.com/api/v0/networks/L_646829496481092083/devices",
#                             headers=headers)
#
# switch = requests.request(method="GET",
#                           url="https://api.meraki.com/api/v0/devices/Q2DP-H886-5KP3/switchPorts",
#                           headers=headers)
#

# print(networks.content)
# print(devices.content)
# print(json.dumps(devices.json(), indent=4))

# I found an unhealthy device here
# for device in devices.json():
#     if device["mac"] == "e0:55:3d:f4:39:3a":
#         print(json.dumps(device, indent=4))

# bad_device = requests.request(method="GET",
#                               url="https://api.meraki.com/api/v0/networks/L_646829496481092083/devices/Q2RD-4ZSU-DLC6/",
#                               headers=headers)
#
#
# print(json.dumps(bad_device.json(), indent=4))

# print(json.dumps(networks.json(), indent=4))

# print(switch.content)

