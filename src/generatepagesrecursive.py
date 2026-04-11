import os
import pathlib

from generatepage import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content):
        dest_dir_path = f"{dest_dir_path[:-2]}html"
        generate_page(dir_path_content, template_path, dest_dir_path)
        return
    items = os.listdir(dir_path_content)
    for item in items:
        nested_source = os.path.join(dir_path_content, pathlib.Path(item))
        nested_destination = os.path.join(dest_dir_path, pathlib.Path(item))
        generate_pages_recursive(nested_source, template_path, nested_destination)