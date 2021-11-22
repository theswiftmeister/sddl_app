import os


class FileIO(object):
    def __init__(self) -> None:
        pass

    def mkdir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
