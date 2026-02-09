class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("the to_html method not implemented")
    
    def props_to_html(self):
        return_string = ""
        if self.props is None:
            return ""
        else:
            for key in self.props:
                return_string += f' {key}="{self.props[key]}"'
        return return_string
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("no value, this is not a leaf node")
        elif self.tag == None:
            return self.value
        else:  
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        children_html = []

        if self.tag == None:
            raise ValueError("no tag")
        elif self.children == None:
            raise ValueError("no children")
        else:
            props_html = self.props_to_html()

        for child in self.children:
            children_html.append(child.to_html())
        
        child_str = ""
        for child_html in children_html:
            child_str += child_html

        str_to_return = f'<{self.tag}{props_html}>{child_str}</{self.tag}>'

        return str_to_return

