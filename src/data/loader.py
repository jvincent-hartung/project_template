"""
Module for loading and managing CSV report data.
"""
from datetime import datetime
import json
from pathlib import Path

import pandas as pd


class ReportLoader:
    """
    Handles loading and management of CSV report data.

    Provides functionality to load batches of CSV files into pandas DataFrames,
    track metadata about the loaded files, and manage batch organization.
    """
    def __init__(self, raw_data_path="data/raw"):
        self.raw_data_path = Path(raw_data_path)
        self.raw_data_path.mkdir(parents=True, exist_ok=True)

    def load_batch(self, batch_name):
        """
        Load a batch of CSV files and return them as DataFrames.

        Args:
            batch_name: Name/identifier for this batch of reports

        Returns:
            Dictionary mapping filenames to DataFrames
        """
        batch_path = self.raw_data_path / batch_name
        if not batch_path.exists():
            raise ValueError(f"Batch directory {batch_name} not found")

        dataframes = {}
        for csv_file in batch_path.glob("*.csv"):
            try:
                df = pd.read_csv(csv_file)
                dataframes[csv_file.name] = df
            except (pd.errors.EmptyDataError, pd.errors.ParserError) as e:
                print(f"Error loading {csv_file}: {e}")

        return dataframes

    def save_batch_metadata(self, batch_name, dataframes):
        """
        Save metadata about the loaded batch for future reference.

        Args:
            batch_name: Name/identifier for this batch
            dataframes: Dictionary of loaded DataFrames
        """
        metadata = {
            "batch_name": batch_name,
            "timestamp": datetime.now().isoformat(),
            "files": list(dataframes.keys()),
            "row_counts": {name: df.shape[0] for name, df in dataframes.items()}
        }

        metadata_path = self.raw_data_path / f"{batch_name}_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)

    def list_available_batches(self):
        """List all available batch directories."""
        return [p.name for p in self.raw_data_path.iterdir() if p.is_dir()]
