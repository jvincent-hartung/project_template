"""
This script sets up a Python virtual environment and installs dependencies from requirements.txt.
"""

import os
import subprocess
import sys


def create_virtual_environment(env_name="venv"):
    """Creates a virtual environment."""
    if not os.path.exists(env_name):
        print(f"Creating virtual environment '{env_name}'...")
        subprocess.check_call([sys.executable, "-m", "venv", env_name])
    else:
        print(f"Virtual environment '{env_name}' already exists.")

def upgrade_pip(env_name="venv"):
    """Upgrades pip to the latest version in the virtual environment."""
    python_path = (
        os.path.join(env_name, "Scripts", "python.exe")
        if os.name == "nt"
        else os.path.join(env_name, "bin", "python")
    )
    print("Upgrading pip to the latest version...")
    try:
        subprocess.check_call([python_path, "-m", "pip", "install", "--upgrade", "pip"])
        print("Pip successfully upgraded.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade pip: {e}")

def install_requirements(env_name="venv", requirements_file="requirements.txt"):
    """Installs the dependencies from requirements.txt."""
    pip_path = (
        os.path.join(env_name, "Scripts", "pip.exe")
        if os.name == "nt"
        else os.path.join(env_name, "bin", "pip")
    )
    if not os.path.exists(requirements_file):
        print(f"{requirements_file} not found. Skipping dependency installation.")
        return
    print(f"Installing dependencies from {requirements_file}...")
    subprocess.check_call([pip_path, "install", "-r", requirements_file])


if __name__ == "__main__":
    VENV_NAME = "venv"  # Changed to conform to UPPER_CASE naming style
    create_virtual_environment(VENV_NAME)
    upgrade_pip(VENV_NAME)
    install_requirements(VENV_NAME)
    print("Setup complete. To activate the virtual environment, run:")
    if os.name == "nt":
        print(f"{VENV_NAME}\\Scripts\\activate")
    else:
        print(f"source {VENV_NAME}/bin/activate")
