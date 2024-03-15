import requests


class Requester:
    def __init__(self, url, headers, cookies):
        self.url = url
        self.headers = headers
        self.cookies = cookies

    def make_get_request(self):
        res = requests.get(url=self.url, headers=self.headers, cookies=self.cookies)
        return res.status_code, res.text
