#!/usr/bin/python
import requests
import sys


requests.packages.urllib3.disable_warnings()

#Credentials for Sandbox NETCONF/RESTCONF and YANG on IOS XE (always-on)
HOST = 'ios-xe-mgmt.cisco.com'
PORT = 9443
USER = 'root'
PASS = 'D_Vay!_10&'


def get_configured_interfaces_state():
    """Retrieving state data from RESTCONF."""
    url = "https://{h}:{p}/restconf/data/ietf-interfaces:interfaces-state".format(h=HOST, p=PORT)
    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    # return the json as text
    return response.text


def main():
    """Simple main method calling our function."""
    state = get_configured_interfaces_state()

    # print the json that is returned
    print(state)

if __name__ == '__main__':
    sys.exit(main())
