from src.request import Requester
import json


def test_make_get_request():
    url = "https://httpbin.org/get"
    headers = {}
    cookies = {}
    request_manager = Requester(url, headers, cookies)

    status_code, res = request_manager.make_get_request()

    assert status_code == 200
    assert list(json.loads(res).keys()) == ["args", "headers", "origin", "url"]
