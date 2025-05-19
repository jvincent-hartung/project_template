"""
Module for opening and comparing analysis results.

Provides functionality to retrieve and compare analysis results
from different batches or analysis methods.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd


class ResultManager:
    """
    Manages retrieval and comparison of analysis results.

    Provides methods to load analysis results from various file formats
    (parquet, JSON, numpy arrays) and compare results across different
    analyses or versions.
    """

    def __init__(self, results_path="data/results"):
        """
        Initialize with path to results directory.

        Args:
            results_path: Path to the directory containing analysis results

        Raises:
            ValueError: If the results directory doesn't exist
        """
        self.results_path = Path(results_path)
        if not self.results_path.exists():
            raise ValueError(
                f"Results directory '{results_path}' not found. "
                "Analyses must be run and saved before they can be managed."
            )

    def _validate_analysis_path(self, analysis_id):
        """
        Validate that an analysis exists and has the expected structure.

        Args:
            analysis_id: ID of the analysis to validate

        Returns:
            Path to the analysis directory

        Raises:
            ValueError: If the analysis doesn't exist or has invalid structure
        """
        analysis_path = self.results_path / analysis_id
        if not analysis_path.exists():
            raise ValueError(
                f"Analysis '{analysis_id}' not found in {self.results_path}")

        # Check for at least one version
        versions = [p for p in analysis_path.iterdir() if p.is_dir()]
        if not versions:
            raise ValueError(
                f"Analysis '{analysis_id}' exists but contains no versions. "
                "The results directory may be corrupted."
            )

        return analysis_path

    def _get_version_path(self, analysis_path, version=None):
        """
        Get the path to a specific version of an analysis.

        Args:
            analysis_path: Path to the analysis directory
            version: Optional version identifier (defaults to latest)

        Returns:
            Path to the version directory

        Raises:
            ValueError: If the specified version doesn't exist
        """
        if version:
            version_path = analysis_path / version
            if not version_path.exists():
                raise ValueError(
                    f"Version {version} not found in {analysis_path.name}"
                )
        else:
            # Get latest version
            versions = sorted(
                p.name for p in analysis_path.iterdir() if p.is_dir())
            if not versions:
                raise ValueError(f"No versions found in {analysis_path.name}")
            version_path = analysis_path / versions[-1]

        return version_path

    def load_analysis(self, analysis_id, version=None):
        """
        Load analysis results, automatically detecting format.
        Could be parquet, json, numpy, etc. based on what's stored.

        Args:
            analysis_id: ID of the analysis to load
            version: Optional version identifier (defaults to latest)

        Returns:
            Dictionary containing loaded results from various file formats
        """
        analysis_path = self._validate_analysis_path(analysis_id)
        version_path = self._get_version_path(analysis_path, version)

        # Load results based on what files exist
        results = {}
        if (version_path / "data.parquet").exists():
            results['data'] = pd.read_parquet(version_path / "data.parquet")
        if (version_path / "model.json").exists():
            with open(version_path / "model.json", encoding='utf-8') as f:
                results['model'] = json.load(f)
        if (version_path / "arrays.npz").exists():
            results['arrays'] = np.load(version_path / "arrays.npz")

        if not results:
            raise ValueError(
                f"No recognized result files found in {version_path}"
            )

        return results
