"""Tests for infrastructure scanner module."""

import unittest
from demeter_infra_scan.infra_scanner import InfraScanner


class TestInfraScanner(unittest.TestCase):
    """Test cases for the InfraScanner class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.scanner = InfraScanner()
    
    def test_scanner_initialization(self):
        """Test that scanner initializes correctly."""
        self.assertIsInstance(self.scanner, InfraScanner)
    
    def test_scan_returns_result(self):
        """Test that scan method returns expected result."""
        result = self.scanner.scan()
        
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)
        self.assertIn('vulnerabilities', result)
        self.assertEqual(result['status'], 'success')
        self.assertIsInstance(result['vulnerabilities'], list)


if __name__ == '__main__':
    unittest.main()
