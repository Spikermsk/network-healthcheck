import requests

key = "093b24e85df15a3e66f1fc359f4c48493eaa1b73"

session = {"X-Cisco-Meraki-API-Key" : key,
           'Content-type': 'Application/json',
           'Accept': 'Application/json'}
#
class Meraki(object):

    def __init__(self, location, serial_number, lan_ip, mac, model, name, network_id, health, clients):
        self.location = location
        self.serial_number = serial_number
        self.lan_ip = lan_ip
        self.mac = mac
        self.model = model
        self.name = name
        self.network_id = network_id
        self.status = health
        self.clients = clients

    def request(self, url):
        return requests.request(method="GET",
                                url=url,
                                headers=session)

    @classmethod
    def from_serial(cls, session, network_id, serial):
        # re-write with aysyncio when you get a moment
        dev = requests.request(method="GET",
                                  url=f"https://api.meraki.com/api/v0/networks/{network_id}/devices/{serial}",
                                  headers=session)

        status = requests.request(method="GET",
                                  url=f"https://api.meraki.com/api/v0/networks/{network_id}/devices/{serial}/uplink",
                                  headers=session)

        locations = requests.request(method="GET",
                                     url="https://api.meraki.com/api/v0/organizations/549236/networks",
                                     headers=session)

        # "https://dashboard.meraki.com/api/v0/devices/{{serial}}/clients?timespan=84000"

        connected_clients = requests.request(method="GET",
                                     url=f"https://api.meraki.com/api/v0/devices/{serial}/clients?timespan=84000",
                                     headers=session)


        clients = connected_clients.json()
        # This will break on multiple interfaces
        health = ""
        location = ""

        #This is an ugly hack for now to get things working
        device = dev.json()

        for i in status.json():
            if "status" in i.keys():
                health = i["status"]

        for l in locations.json():
            if l["id"] == network_id:
                location = l["name"]
                break

        lan_ip = "No IP Discovered"
        if "lanIP" in device.keys():
            lan_ip = device["lanIp"]

        return cls(location=location, serial_number=serial, lan_ip=lan_ip, mac=device["mac"],
                   model=device["model"], name=device["name"], network_id=device["networkId"], health=health,
                   clients=clients)


class AccessPoint(Meraki):
    pass

class Switch(Meraki):
    @property
    def switchports(self):
        return self.request(url=f"https://api.meraki.com/api/v0/devices/{self.serial_number}/switchPorts").json()


class SecurityAppliance(Meraki):
    pass


def main():
    test = AccessPoint.from_serial(session=session, network_id="L_646829496481092083", serial="Q2RD-4ZSU-DLC6")

    # print(type(test))

    print(test.clients)
    print(test.location)

if __name__ == "__main__":
    main()