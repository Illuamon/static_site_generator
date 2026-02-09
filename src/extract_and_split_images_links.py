import re
from textnode import TextType, TextNode

def extract_markdown_images(text):

    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):

    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_list = []
    for old_node in old_nodes:
        current_text = old_node.text
        if not old_node.text_type == TextType.TEXT:
            new_list.append(old_node)
            continue
        else:
            split_nodes = []
            image_extracted = extract_markdown_images(current_text)
            if not image_extracted:
                new_list.append(old_node)
                continue
            else:
                for img in image_extracted:
                    img_markdown = f"![{img[0]}]({img[1]})"
                    sections = current_text.split(img_markdown, 1)
                    before = sections[0]
                    if before == "":
                        split_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
                        current_text = sections[1]
                        continue
                    else:
                        split_nodes.append(TextNode(before, TextType.TEXT))
                    split_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
                    current_text = sections[1]
                if current_text:
                    split_nodes.append(TextNode(current_text, TextType.TEXT))
            new_list.extend(split_nodes)
    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    for old_node in old_nodes:
        current_text = old_node.text
        if not old_node.text_type == TextType.TEXT:
            new_list.append(old_node)
            continue
        else:
            split_nodes = []
            link_extracted = extract_markdown_links(current_text)
            if not link_extracted:
                new_list.append(old_node)
                continue
            else:
                for link in link_extracted:
                    link_markdown = f"[{link[0]}]({link[1]})"
                    sections = current_text.split(link_markdown, 1)
                    before = sections[0]
                    if before == "":
                        split_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                        current_text = sections[1]
                        continue
                    else:
                        split_nodes.append(TextNode(before, TextType.TEXT))
                    split_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                    current_text = sections[1]
                if current_text:
                    split_nodes.append(TextNode(current_text, TextType.TEXT))
            new_list.extend(split_nodes)
    return new_list
