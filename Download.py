
import os
import io
import zipfile
import requests

from PyQt5.QtCore import QThread




class Downloader(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        version_right_now = open("version_right_now.txt", "wb")
        f = open("version.txt", "r")
        version1 = f.read()


        version_right_now.write(version1.encode())
        version_right_now.close()
        r = requests.get(
            "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1wIWx1YX04i8ELmI0zOKxr6KEepHpwLFf")
        with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
            archive.extractall('output')
        f.close()
        r.close()
        os.remove("version.txt")






