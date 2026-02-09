from split_nodes_delimiter import split_nodes_delimiter
from extract_and_split_images_links import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType

def text_to_textnodes(text):
    first_node = TextNode(text, TextType.TEXT)
    nodes = [first_node]
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


            
