#!/usr/bin/env python3

import unittest

from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):  
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovela"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

# Run the tests
unittest.main()
