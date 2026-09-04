# test_nodehinge.py
"""
Tests for NodeHinge module.
"""

import unittest
from nodehinge import NodeHinge

class TestNodeHinge(unittest.TestCase):
    """Test cases for NodeHinge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeHinge()
        self.assertIsInstance(instance, NodeHinge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeHinge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
