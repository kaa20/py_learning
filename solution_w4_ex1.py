import os
import tempfile

class File:

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        if not os.path.exists(self.path_to_file):
            with open(self.path_to_file, 'w'):
                pass


    def read(self):
        with open(self.path_to_file, 'r') as f:
            text = f.read()
        return text

    def write(self, some_str):
        with open(self.path_to_file, 'w') as f:
            f.write(some_str)

    def __add__(self, obj):
        with tempfile.NamedTemporaryFile() as ntf:
            file_storage = os.path.join(tempfile.gettempdir(), ntf.name)
        new_file = File(file_storage)
        new_file.write(self.read() + obj.read())
        return new_file

    def __str__(self):
        return self.path_to_file

    def __iter__(self):
        file = open(self.path_to_file)
        return iter(file)
