import os
import urllib.request



def find_update():
        version_right_now = open('version_right_now.txt', 'r')
        logo = urllib.request.urlopen(
                "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1b85XYQ7P7SgokKfpAqoKbKIATDpYBAHa").read()
        f = open("version.txt", "wb")
        f.write(logo)
        f.close()

        f = open("version.txt", "r")
        version1 = f.read()
        version2 = version_right_now.read()
        version_right_now.close()
        f.close()


        if version1 == version2:
                print("new")
                os.remove("version.txt")
                return True

        else:
                print("not new")
                return False



       

      