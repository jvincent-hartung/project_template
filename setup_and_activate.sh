#!/bin/bash

# Ensure the script is being sourced
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Error: This script must be sourced. Run it as:"
    echo "source ./setup_and_activate.sh"
    exit 1
fi

# Run the setup_env.py script
echo "Running setup_env.py..."
py src/setup_env.py

# Check if the virtual environment exists
if [ -d "venv" ]; then
    echo "Virtual environment found. Attempting to activate..."
    
    # Check the operating system and activate the virtual environment
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        echo "OSTYPE: $OSTYPE"
        echo "Checking for venv/Scripts/activate..."
        ls -l venv/Scripts/activate
        if [ -f "venv/Scripts/activate" ]; then
            source venv/Scripts/activate
            echo "Virtual environment activated."
        else
            echo "Error: Activation script not found in venv/Scripts."
            return 1
        fi
    else
        echo "OSTYPE: $OSTYPE"
        echo "Checking for venv/bin/activate..."
        ls -l venv/bin/activate
        if [ -f "venv/bin/activate" ]; then
            source venv/bin/activate
            echo "Virtual environment activated."
        else
            echo "Error: Activation script not found in venv/bin."
            return 1
        fi
    fi
else
    echo "Error: Virtual environment not found. Please check the setup_env.py script."
    return 1
fi