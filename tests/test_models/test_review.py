#!/usr/bin/python3
"""Defines unittests for review.py"""


import os
import models
import unittest
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_place_id_is_public_class_attribute(self):
        rv = Review(place_id="test_place_id")
        self.assertEqual(str, type(rv.place_id))
        self.assertEqual("test_place_id", rv.place_id)

    def test_user_id_is_public_class_attribute(self):
        rv = Review(user_id="test_user_id")
        self.assertEqual(str, type(rv.user_id))
        self.assertEqual("test_user_id", rv.user_id)

    def test_text_is_public_class_attribute(self):
        rv = Review(text="test_text")
        self.assertEqual(str, type(rv.text))
        self.assertEqual("test_text", rv.text)


if __name__ == "__main__":
    unittest.main()
