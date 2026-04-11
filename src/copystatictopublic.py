import os
import shutil

def copy_static_to_public():
    shutil.rmtree("public/")
    os.mkdir("public/")
    copy_files("static/")

def copy_files(path):
    public_path = f"public{path[6:]}"
    if os.path.isfile(path):
        shutil.copy(path, public_path)
        return
    if not os.path.exists(public_path):
        os.mkdir(public_path)
    items = os.listdir(path)
    for item in items:
        item_path = os.path.join(path, item)
        copy_files(item_path)