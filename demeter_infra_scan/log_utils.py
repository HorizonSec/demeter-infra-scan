"""Shared logging utilities for DEMETER Infrastructure Scanning."""

import logging
import sys


def setup_logging(verbose=False):
    """
    Setup logging configuration.
    
    Args:
        verbose: If True, set logging level to DEBUG, otherwise INFO
        
    Returns:
        The root logger instance
    """
    level = logging.DEBUG if verbose else logging.INFO
    
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    logger = logging.getLogger("demeter_infra_scan")
    logger.setLevel(level)
    
    return logger
