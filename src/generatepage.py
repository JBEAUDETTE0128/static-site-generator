import os
from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as markdown_file:
        markdown = markdown_file.read()
    with open(template_path) as template_file:
        template = template_file.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template_with_title = template.replace("{{ Title }}", title)
    template_with_content = template_with_title.replace("{{ Content }}", html)
    template_with_href = template_with_content.replace('href="/', f'href={basepath}')
    webpage = template_with_href.replace('src="/', f'src="{basepath}')
    destination_directory = os.path.dirname(dest_path)
    os.makedirs(destination_directory, 0o777, True)
    destination_file = open(dest_path, "w")
    destination_file.write(webpage)
    destination_file.close()