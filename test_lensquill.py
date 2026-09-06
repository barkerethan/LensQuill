# test_lensquill.py
"""
Tests for LensQuill module.
"""

import unittest
from lensquill import LensQuill

class TestLensQuill(unittest.TestCase):
    """Test cases for LensQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LensQuill()
        self.assertIsInstance(instance, LensQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LensQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
