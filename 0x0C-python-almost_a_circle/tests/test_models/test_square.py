# #!/usr/bin/python3

# """Defines unittests for models/square.py."""

# import io
# import sys
# import unittest
# from models.base import Base
# from models.square import Square


# class TestSquare_instantiation(unittest.TestCase):
#     """Unittests for testing instantiation of the Square class."""

#     def test_is_base(self):
#         self.assertIsInstance(Square(10), Base)

#     def test_is_rectangle(self):
#         self.assertIsInstance(Square(10), Square)

#     def test_no_args(self):
#         with self.assertRaises(TypeError):
#             Square()
