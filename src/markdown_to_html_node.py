from htmlnode import ParentNode, HTMLNode, LeafNode
from blocktypes import block_to_block_type, markdown_to_blocks, BlockType
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node

def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            paragraph_text = block
            paragraph_text = paragraph_text.replace("\n", " ")
            block_node = ParentNode("p", children=text_to_children(paragraph_text))

        elif block_type == BlockType.CODE:
            code_text = block
            code_text = code_text.strip("```\n")
            code_text += "\n"
            block_node = ParentNode("pre", children=[LeafNode("code", code_text)])

        elif block_type == BlockType.HEADING:
            heading_text = block
            hashtags = ""
            for char in heading_text:
                if char == "#":
                    hashtags += char
                else:
                    break
            heading_text = heading_text.strip(f"{hashtags} ")
            heading_text = heading_text.lstrip()
            block_node = ParentNode(f"h{len(hashtags)}", children=text_to_children(heading_text))

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned = []
            for line in lines:
                line = line.lstrip()
                if line.startswith(">"):
                    line = line[1:]
                    if line.startswith(" "):
                        line = line[1:]
                cleaned.append(line)
            quote_text = "\n".join(cleaned)
            block_node = ParentNode("blockquote", children=text_to_children(quote_text)) 

        elif block_type == BlockType.ULIST:
            olist_text = block
            lines = olist_text.split("\n")
            line_nodes = []
            for line in lines:
                line = line.lstrip()
                if line.startswith("- "):
                    line = line[2:]
                elif line.startswith("-"):
                    line = line[1:]
                line_nodes.append(ParentNode("li", children=text_to_children(line)))
            block_node = ParentNode("ul", children=line_nodes)
        
        elif block_type == BlockType.OLIST:
            olist_text = block
            lines = olist_text.split("\n")
            line_nodes = []
            for line in lines:
                line = line.lstrip()
                j = 0
                while j < len(line) and line[j].isdigit():
                    j += 1
                if j > 0 and j < len(line) and line[j] == ".":
                    line = line[j+1:]
                    if line.startswith(" "):
                        line = line[1:]
                line_nodes.append(ParentNode("li", children=text_to_children(line)))
            block_node = ParentNode("ol", children=line_nodes)
        
        else:
            raise Exception("block type not recognized")
        
        children.append(block_node)

    parent = ParentNode("div", children=children)
    return parent

    
