import os
import shutil

def copy_static(destination):
    if os.path.exists(f"{destination}/"):
        shutil.rmtree(f"{destination}/")
    os.mkdir(f"{destination}/")
    copy_files(destination, "static/")

def copy_files(destination, path):
    public_path = f"{destination}{path[6:]}"
    if os.path.isfile(path):
        shutil.copy(path, public_path)
        return
    if not os.path.exists(public_path):
        os.mkdir(public_path)
    items = os.listdir(path)
    for item in items:
        item_path = os.path.join(path, item)
        copy_files(destination, item_path)