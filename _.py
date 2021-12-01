import json
import base64
import os
from collections import ChainMap


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


# l = [
#     {'name': '2', 'rows': [['27/11/2021', 'a', 'q', '3', '2', '6.00']]},
#     {'name': '1', 'rows': [['27/11/2021', '3', '3', '3', '3', '9.00']]},
#     {'name': '3', 'rows': []},
#     {'name': '4', 'rows': []}]


# print([i["name"] for i in l])

l = [{'name': '1', 'unit': {'a': '2', 'a2': '2', 'a5': '2', 'a6': '2'},
     'rows': [["a", 1, 2, 3, 4, 5], ["a", 1, 2, 3, 4, 5], ["a", 1, 2, 3, 4, 5]]}, {'name': '1', 'unit': {'a': '2', 'a2': '2', 'a5': '2', 'a6': '2'},
                                                                                   'rows': [["a", 1, 2, 3, 4, 5], ["a", 1, 2, 3, 4, 5], ["a", 1, 2, 3, 4, 5]]}, {'name': '1', 'unit': {'a': '2', 'a2': '2', 'a5': '2', 'a6': '2'},
                                                                                                                                                                 'rows': [["a", 1, 2, 3, 4, 5], ["a", 1, 2, 3, 4, 5], ["a", 1, 2, 3, 4, 5]]}]

# for i in l:
#     for r in i["rows"]:
#         print(r, end="\n")

a = [r for r in [i["rows"] for i in l]]
print(a)
