import json


class JsonConfig:
    def __init__(self, file_name="conf/devices.json"):
        self.devices = self._load_devices(file_name)

    def get_name(self, mac):
        return self.devices[mac]['name']

    def get_appear_action(self, mac):
        try:
            return self.devices[mac]['on']['appear']
        except KeyError:
            pass

    def get_lost_action(self, mac):
        try:
            return self.devices[mac]['on']['lost']
        except KeyError:
            pass

    @staticmethod
    def _load_devices(file_name):
        js = open(file_name)
        result = {}
        for mac, data in json.load(js).iteritems():
            result[mac.lower()] = data
        return result
