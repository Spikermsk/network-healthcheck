#!/usr/bin/python

import requests
import sys

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

#Credentials for Sandbox NETCONF/RESTCONF and YANG on IOS XE (always-on)
HOST = 'ios-xe-mgmt.cisco.com'
PORT = 9443
USER = 'root'
PASS = 'D_Vay!_10&'


# create a main() method
def main():
    """Main method that retrieves statistic information via RESTCONF."""

    # url string to issue GET request
    url = "https://{h}:{p}/restconf/data/ietf-netconf-monitoring:netconf-state/statistics".format(h=HOST, p=PORT)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    # print the json that is returned
    print(response.text)

if __name__ == '__main__':
    sys.exit(main())
