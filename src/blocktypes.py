from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        stripped = block.strip()
        stripped = stripped.strip("\n")
        if stripped:
            stripped_blocks.append(stripped)
    return stripped_blocks

def block_to_block_type(block):
    if re.findall(r"^\#{1,6}\ ", block):
        return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    block_copy = block
    block_copy = block_copy.split("\n")
    is_quote = True
    for line in block_copy:
        if line.startswith(">") == False:
            is_quote = False
    if is_quote:
        return BlockType.QUOTE
    
    is_ulist = True
    for line in block_copy:
        if line.startswith("- ") == False:
            is_ulist = False
    if is_ulist:
        return BlockType.ULIST
    
    is_olist = True
    index = 0
    for line in block_copy:
        index += 1
        if line.startswith(f"{index}. ") == False:
            is_olist = False
    if is_olist:
        return BlockType.OLIST
    
    return BlockType.PARAGRAPH

