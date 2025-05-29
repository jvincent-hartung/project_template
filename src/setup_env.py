"""
This script sets up a Python virtual environment and installs dependencies from requirements.txt.
"""

import os
import subprocess
import sys
from pathlib import Path

# Base constants
ROOT = Path()
SRC_NAME = "src"
ENV_NAME = "venv"
REQUIREMENTS_FILE = "requirements.txt"

# Platform-specific constants (determined once, used everywhere)
IS_WINDOWS = os.name == "nt"
PYTHON_EXE = "python.exe" if IS_WINDOWS else "python"
PIP_EXE = "pip.exe" if IS_WINDOWS else "pip"
VENV_SCRIPTS_DIR = "Scripts" if IS_WINDOWS else "bin"

# Derived paths (now consistent and complete)
ROOT_PATH = ROOT
SRC_PATH = ROOT / SRC_NAME
VENV_PATH = ROOT / ENV_NAME
VENV_PYTHON_PATH = VENV_PATH / VENV_SCRIPTS_DIR / PYTHON_EXE
VENV_PIP_PATH = VENV_PATH / VENV_SCRIPTS_DIR / PIP_EXE
REQUIREMENTS_PATH = ROOT / REQUIREMENTS_FILE


def create_virtual_environment():
    """Creates a virtual environment."""
    if not VENV_PATH.exists():
        print(f"Creating virtual environment '{ENV_NAME}'...")
        subprocess.check_call([sys.executable, "-m", "venv", str(VENV_PATH)])
    else:
        print(f"Virtual environment '{ENV_NAME}' already exists.")


def upgrade_pip():
    """Upgrades pip to the latest version in the virtual environment."""
    print("Upgrading pip to the latest version...")
    try:
        subprocess.check_call(
            [str(VENV_PYTHON_PATH), "-m", "pip", "install", "--upgrade", "pip"])
        print("Pip successfully upgraded.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade pip: {e}")


def install_requirements():
    """Installs the dependencies from requirements.txt."""
    if not REQUIREMENTS_PATH.exists():
        print(f"{REQUIREMENTS_FILE} not found. Skipping dependency installation.")
        return

    print(f"Installing dependencies from {REQUIREMENTS_FILE}...")
    try:
        subprocess.check_call(
            [str(VENV_PIP_PATH), "install", "-r", str(REQUIREMENTS_PATH)])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")

def install_modules():
    """
    This will install our src directory as modules in dev mode,
    which enables us to import them directly into other files like our tests
    """
    print("Installing src directory as a module in development mode...")
    try:
        subprocess.check_call(
            [str(VENV_PIP_PATH), "install", "-e", str(ROOT_PATH)])
        print("Src directory installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install src directory: {e}")

if __name__ == "__main__":
    create_virtual_environment()
    upgrade_pip()
    install_requirements()
    install_modules()
    print(f"Setup complete. To activate the virtual environment, run: {VENV_SCRIPTS_DIR}/activate")
