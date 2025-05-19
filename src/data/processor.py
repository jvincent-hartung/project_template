"""
Module for processing and transforming loaded data.
"""
from pathlib import Path
import pandas as pd


class DataProcessor:
    """
    Processes and transforms loaded data, saving results in parquet format.

    Handles batch processing of DataFrames, applying transformations and managing
    the storage of processed data in a structured directory format.
    """

    def __init__(self, processed_data_path="data/processed"):
        self.processed_data_path = Path(processed_data_path)
        if not self.processed_data_path.exists():
            raise ValueError(
                f"Data directory '{processed_data_path}' not found. "
                "Create it first or check the path for typos."
            )

    def create_data_directory(self):
        """Create the data directory if it doesn't exist."""
        self.processed_data_path.mkdir(parents=True, exist_ok=True)

    def process_batch(self, dataframes, batch_name, transformations=None):
        """
        Process a batch of DataFrames with specified transformations.

        Args:
            dataframes: Dictionary of DataFrames to process
            batch_name: Name/identifier for this batch
            transformations: List of transformation configurations

        Returns:
            Dictionary of processed DataFrames
        """
        processed = {}

        for name, df in dataframes.items():
            processed_df = df.copy()

            if transformations:
                for _ in transformations:  # Using _ for unused variable
                    # Apply specified transformations
                    # Example: aggregations, filtering, etc.
                    pass

            processed[name] = processed_df

        # Save processed DataFrames
        self.save_processed_batch(processed, batch_name)
        return processed

    def save_processed_batch(self, processed_dfs, batch_name):
        """
        Save processed DataFrames to the processed data directory using Parquet format.
        Uses 'snappy' compression by default for good balance of compression ratio and speed.
        """
        batch_dir = self.processed_data_path / batch_name
        batch_dir.mkdir(exist_ok=True)

        for name, df in processed_dfs.items():
            try:
                df.to_parquet(
                    batch_dir / f"{name}.parquet",
                    compression='snappy'
                )
            except Exception as e:
                raise ValueError(f"Error saving {name} to parquet: {str(e)}") from e

    def load_processed_batch(self, batch_name):
        """Load a previously processed batch of data."""
        batch_dir = self.processed_data_path / batch_name
        if not batch_dir.exists():
            raise ValueError(f"Processed batch {batch_name} not found")

        processed = {}
        for parquet_file in batch_dir.glob("*.parquet"):
            processed[parquet_file.stem] = pd.read_parquet(parquet_file)

        return processed
