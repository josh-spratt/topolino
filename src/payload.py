import json
import urllib.parse


class PayloadBuilder:
    def __init__(self):
        self.payload = {}

    def collect_parameter(self, prompt):
        value = input(f"{prompt}: ")
        key = prompt
        self.payload[key] = value

    def add_static_parameter(self, key, value):
        self.payload[key] = value

    def manipulate_payload(self):
        json_querystring = str(json.dumps(self.payload))
        encoded_str = urllib.parse.quote(json_querystring)
        return dict(roomForm_jar=encoded_str)
