import unittest
from blocktypes import block_to_block_type, BlockType


class TestBlockTypes(unittest.TestCase):
    def test_quote(self):
        block = """> this should be a quote
> this too
this as well"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()