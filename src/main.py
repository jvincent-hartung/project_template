"""
Main script for processing CSV reports into parquet format.
"""
import sys

import pandas as pd
import structlog

from src.data.loader import ReportLoader
from src.data.processor import DataProcessor

# Configure structured logging
logger = structlog.get_logger()


def process_batch(batch_name):
    """
    Process a batch of CSV files into parquet format.

    Args:
        batch_name: Name of the batch directory under data/raw/
    """
    log = logger.bind(batch_name=batch_name)
    loader = ReportLoader()
    processor = DataProcessor()

    log.info("loading_csv_files")
    try:
        dataframes = loader.load_batch(batch_name)
    except ValueError as e:
        log.error("batch_load_failed", error=str(e))
        return

    if not dataframes:
        log.warning("no_csv_files_found")
        return

    log.info("loaded_csv_files", file_count=len(dataframes))

    # Save metadata about the loaded files
    loader.save_batch_metadata(batch_name, dataframes)

    log.info("processing_files")
    try:
        processor.process_batch(dataframes, batch_name)
        log.info("batch_processing_complete", output_dir=f"data/processed/{batch_name}/")
    except (ValueError, pd.errors.EmptyDataError, OSError) as e:
        log.error("batch_processing_failed", error=str(e))


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python -m src.main <batch_name>")
        print("Example: python -m src.main may_2025")
        sys.exit(1)

    batch_name = sys.argv[1]
    process_batch(batch_name)


if __name__ == "__main__":
    main()
