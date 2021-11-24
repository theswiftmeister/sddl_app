import os
import json


class FileIO:
    def __init__(self) -> None:
        pass

    def save(self, path, file_name, file_type, data):
        with open(f"{path}/{file_name}{file_type}", "w", encoding="utf-8") as file:
            _json = json.dumps(data)
            file.write(_json)
            file.close()

    def load(self, path, file_name, file_type):
        with open(f"{path}/{file_name}{file_type}", "r", encoding="utf-8") as file:
            _json = json.loads(file.read())
            file.close()
        return _json

    def mkdir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def create_project_files(self, file_names, path, file_type):
        for name in file_names:
            self.create_file(name, path, file_type)

    def create_file(self, file_name, path, file_type):
        file = open(f"{path}/{file_name}{file_type}",
                    "w", encoding="utf-8")
        file.write("[]")
        file.close()

    def get_project_files(self, path):
        if os.path.isdir(path):
            return os.listdir(path)
