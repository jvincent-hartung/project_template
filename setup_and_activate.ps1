# Ensure Python is available
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed or not in PATH. Please install Python and try again." -ForegroundColor Red
    exit 1
}

# Run the setup_env.py script
Write-Host "Running setup_env.py to ensure everything is set up..."
python .\src\setup_env.py

# Check if the virtual environment exists
if (-Not (Test-Path -Path ".\venv")) {
    Write-Host "Virtual environment not found. Please check the setup_env.py script." -ForegroundColor Red
    exit 1
}

# Activate the virtual environment
Write-Host "Activating the virtual environment..."
.\venv\Scripts\Activate

# Confirm activation
Write-Host "Virtual environment activated. You should see '(venv)' in your terminal prompt."