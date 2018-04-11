import json

class AccessPoint(object):
    def cpu_green(self):
        return json.dumps({"cpu_utilization": "15", "ram_utilization": "15"})

    def cpu_red(self):
        return json.dumps({"cpu_utilization": "85", "ram_utilization": "95"})

    def cpu_yellow(self):
        return json.dumps({"cpu_utilization": "55", "ram_utilization": "75"})

    def interface_green(self):
        return json.dumps({"state": "up", "duplex": "full", "link_util": "25", "error_rate ": "0"})

    def interface_yellow(self):
        return json.dumps({"state": "up", "duplex": "full", "link_util": "25", "error_rate ": "5"})

    def interface_red(self):
        return json.dumps({"state": "up", "duplex": "half", "link_util": "99", "error_rate ": "50"})

class Switch(object):


    def cpu_green(self):
        return json.dumps({"cpu_utilization": "15", "ram_utilization": "15"})

    def cpu_red(self):
        return json.dumps({"cpu_utilization": "85", "ram_utilization": "95"})

    def cpu_yellow(self):
        return json.dumps({"cpu_utilization": "55","ram_utilization": "75"})

    def interface_green(self):
        return json.dumps({"state": "up", "duplex": "full", "link_util": "25", "error_rate ": "0"})

    def interface_yellow(self):
        return json.dumps({"state": "up", "duplex": "full", "link_util": "25", "error_rate ": "5"})

    def interface_red(self):
        return json.dumps({"state": "up", "duplex": "half", "link_util": "99", "error_rate ": "50"})

class Router(object):
    def cpu_green(self):
        return json.dumps({"cpu_utilization": "15", "ram_utilization": "15"})

    def cpu_red(self):
        return json.dumps({"cpu_utilization": "85", "ram_utilization": "95"})

    def cpu_yellow(self):
        return json.dumps({"cpu_utilization": "55", "ram_utilization": "75"})

    def interface_green(self):
        return json.dumps({"state": "up", "duplex": "full", "link_util": "25", "error_rate ": "0"})

    def interface_yellow(self):
        return json.dumps({"state": "up", "duplex": "full", "link_util": "25", "error_rate ": "5"})

    def interface_red(self):
        return json.dumps({"state": "up", "duplex": "half", "link_util": "99", "error_rate ": "50"})


