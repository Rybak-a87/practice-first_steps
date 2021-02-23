from zipfile import ZipFile
import os


def zip(path, zpath):
    zfile = ZipFile(zpath, "w")
    if os.path.isfile(path):
        zfile.write(path)
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                zfile.write(f"{root}/{file}")
    zfile.close()


def anzip(path, zpath):
    zfile = ZipFile(zpath, "r")
    for name in zfile.namelist():
        dir, file = os.path.split(name)
        if not os.path.exists(f"{path}/{dir}"):
            os.mkdir(f"{path}/{dir}")
        if file:
            handler = open(f"{path}/{name}", "wb")
            handler.write(zfile.read(name))
            handler.close()
    zfile.close()



# zip("temp/", "my.zip")
# anzip("abc", "my.zip")