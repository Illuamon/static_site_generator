from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for old_node in old_nodes:
        if not old_node.text_type == TextType.TEXT:
            new_list.append(old_node)
        else:
            split_nodes = []
            splitted = old_node.text.split(delimiter)

            if len(splitted) % 2 == 0:
                raise Exception("invalid markdown syntax, odd number of delimiters")
            
            for i in range(len(splitted)):
                if splitted[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(splitted[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(splitted[i], text_type))
            new_list.extend(split_nodes)

    return new_list

