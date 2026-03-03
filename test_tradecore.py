# test_tradecore.py
"""
Tests for TradeCore module.
"""

import unittest
from tradecore import TradeCore

class TestTradeCore(unittest.TestCase):
    """Test cases for TradeCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TradeCore()
        self.assertIsInstance(instance, TradeCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TradeCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
