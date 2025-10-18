"""CLI entry point for DEMETER Infrastructure Scanning."""

import argparse
from demeter_infra_scan import __version__
from horizon_core.logging import setup_logging
from demeter_infra_scan.infra_scanner import InfraScanner


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="DEMETER Infrastructure Scanning CLI"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"demeter-infra-scan {__version__}"
    )
    parser.add_argument(
        "--scan",
        help="Scan infrastructure configuration",
        action="store_true"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        help="Enable verbose logging",
        action="store_true"
    )
    
    args = parser.parse_args()
    
    # Setup logging using horizon-core
    log_level = "DEBUG" if args.verbose else "INFO"
    setup_logging(level=log_level)
    
    if args.scan:
        scanner = InfraScanner()
        scanner.scan()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
