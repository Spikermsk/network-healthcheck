#!/usr/bin/env python
from getpass import getpass
import requests
import json
from meraki.classes import Meraki, AccessPoint, Switch, SecurityAppliance

# key = getpass("Enter API key:")

# sandbox API key

key = "542ed166c361826ad9a7f9d3038090eabb146728"

headers = {"X-Cisco-Meraki-API-Key" : key,
           'Content-type': 'Application/json',
           'Accept': 'Application/json'}
#
# org = requests.request(method="GET",
#                        url="https://api.meraki.com/api/v0/organizations",
#                        headers=headers)
# #
# print(json.dumps(org.json(), indent=4))
# #
# #
# networks = requests.request(method="GET",
#                             url="https://api.meraki.com/api/v0/organizations/183001/networks",
#                             headers=headers)
#
# print(json.dumps(networks.json(), indent=4))

# checking for good
# 681155 has devices
#
# networks = requests.request(method="GET",
#                             url="https://api.meraki.com/api/v0/organizations/681155/networks",
#                             headers=headers)
#
# print(networks.content)

# print(json.dumps(networks.json(), indent=4))


# for network in networks.json():
#     net_id = network["id"]
#     devices = requests.request(method="GET",
#                                url=f"https://api.meraki.com/api/v0/networks/{net_id}/devices",
#                                headers=headers)
#
#     for device in devices.json():
#         inventory.append(Meraki.from_serial(session=headers, network_id=net_id, serial=device["serial"]))



    #
    # print("#" + network["name"])
    # print(json.dumps(devices.json(), indent=4))
    # print("#" * 80)
# print(json.dumps(networks.json()))
# #
# #
# devices = requests.request(method="GET",
#                             url="https://api.meraki.com/api/v0/networks/L_582090251837636767/devices",
#                             headers=headers)
#
#
# inventory = []
# for device in devices.json():
#     inventory.append(Meraki.from_serial(session=headers, network_id="L_582090251837636767", serial=device["serial"]))
#
# for i in inventory:
#     print(i.status)


print(Meraki.get_all_locations())

# print(inventory)
#
# for thing in inventory:
#     print(thing.model, thing.serial_number, thing.lan_ip)

# print(json.dumps(devices.json(), indent=4))

# switch = requests.request(method="GET",
#                           url="https://api.meraki.com/api/v0/devices/Q2HP-WH5E-MK7H/switchPorts",
#                           headers=headers)
#
# myswitch = Switch.from_serial(session=headers, network_id="L_646829496481092083", serial="Q2HP-WH5E-MK7H")
#
#
# # print(myswitch.switchports)
#
# for i in myswitch.switchports:
#     print(i["number"], i["enabled"])


# dir(myswitch)
# print(myswitch.switchports())
# print(json.dumps(switch.json(), indent=4))
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

