from textnode import TextNode, TextType
from blocktypes import markdown_to_blocks, BlockType, block_to_block_type
from markdown_to_html_node import markdown_to_html_node

import os
import shutil

def main():
    copy_files("./static", "./public")
    generate_pages_recursive("content", "template.html", "public")


def copy_files(source, destination):
    if os.path.exists(destination) and os.path.exists(source):
        shutil.rmtree(destination)
        os.mkdir(destination)
        files_in_src = os.listdir(source)
        for file in files_in_src:
            better_path_file = os.path.join(source, file)
            check = os.path.isfile(better_path_file)
            if check:
                shutil.copy(better_path_file, destination)
            else:
                new_dest = os.path.join(destination, file)
                new_src = os.path.join(source, file)
                os.mkdir(new_dest)
                copy_files(new_src, new_dest)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            if block.startswith("# "):
                title = block.strip("# ")
                return title.strip()
    raise Exception("no h1 header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if os.path.exists(from_path) and os.path.exists(template_path):
        with open(from_path, 'r') as f:
            markdown = f.read()
            f.close()
        with open(template_path, 'r') as f:
            template = f.read()
            f.close
        content = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)
        
        w_title = template.replace("{{ Title }}", title)
        full_html = w_title.replace("{{ Content }}", content)

        if os.path.exists(os.path.dirname(dest_path)):
            with open(dest_path, 'w') as f:
                f.write(full_html)
                f.close()
        else:
            os.makedirs(os.path.dirname(dest_path))
            with open(dest_path, 'w') as f:
                f.write(full_html)
                f.close()
    else:
        raise Exception("from path, template or both dont exist")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.exists(dir_path_content) and os.path.exists(template_path):
        if not os.path.exists(dest_dir_path):
            os.makedirs(dest_dir_path)
        level_content = os.listdir(dir_path_content)
        for item in level_content:
            item_path = os.path.join(dir_path_content, item)
            if os.path.exists(item_path) and item_path.endswith(".md"):
                #generate html
                new_dest = os.path.join(dest_dir_path, item.replace(".md", ".html"))
                generate_page(item_path, template_path, new_dest)
            elif os.path.exists(item_path) and os.path.isdir(item_path):
                new_dest = os.path.join(dest_dir_path, item)
                print(f"going into dir {item_path}")
                generate_pages_recursive(item_path, template_path, new_dest)
            else:
                continue          
    else:
        raise Exception("one of the paths does not exist")

main()
