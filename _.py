import json
import base64
import os


def encode(data):
    with open("test.sb", 'w', encoding='utf-8') as file:
        _json = json.dumps(data)
        j_bytes = _json.encode("utf-8")
        base_encode = base64.a85encode(j_bytes)
        file.write(base_encode.decode("utf-8"))


def decode():
    with open("test.sb", 'r', encoding='utf-8') as file:
        j_bytes = file.read().encode("utf-8")
        base_decode = base64.a85decode(j_bytes)
        _json = json.loads(base_decode)
        print(_json)


print(os.getenv("USER_NAME"))
