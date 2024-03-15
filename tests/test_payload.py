from src.payload import PayloadBuilder
import urllib
import json


def test_collect_parameter(monkeypatch):
    builder = PayloadBuilder()
    expected_value = "tester test"
    monkeypatch.setattr("builtins.input", lambda _: expected_value)
    prompt = "Enter a test value..."
    builder.collect_parameter(prompt)
    assert builder.payload[prompt] == expected_value


def test_add_static_parameter():
    builder = PayloadBuilder()
    static_key = "key"
    static_value = "value"
    builder.add_static_parameter(static_key, static_value)
    assert builder.payload[static_key] == static_value


def test_manipulate_payload():
    builder = PayloadBuilder()
    builder.payload = {"test_key": "test_value"}
    manipulated_payload = builder.manipulate_payload()

    expected_encoded_str = urllib.parse.quote(json.dumps(builder.payload))
    assert manipulated_payload == {"roomForm_jar": expected_encoded_str}
