"""Tests for CLI module."""

import unittest
from unittest.mock import patch, MagicMock
from demeter_infra_scan.cli import main


class TestCLI(unittest.TestCase):
    """Test cases for the CLI module."""
    
    def test_version_flag(self):
        """Test --version flag displays version."""
        with patch('sys.argv', ['demeter', '--version']):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 0)
    
    def test_help_flag(self):
        """Test --help flag displays help."""
        with patch('sys.argv', ['demeter', '--help']):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 0)
    
    @patch('demeter_infra_scan.cli.setup_logging')
    @patch('demeter_infra_scan.cli.InfraScanner')
    def test_scan_flag(self, mock_scanner_class, mock_setup_logging):
        """Test --scan flag triggers scanning."""
        mock_scanner = MagicMock()
        mock_scanner_class.return_value = mock_scanner
        
        with patch('sys.argv', ['demeter', '--scan']):
            main()
        
        mock_scanner_class.assert_called_once()
        mock_scanner.scan.assert_called_once()
        mock_setup_logging.assert_called_once_with(level='INFO')


if __name__ == '__main__':
    unittest.main()
