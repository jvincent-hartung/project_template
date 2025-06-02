# Python Project Template

A comprehensive template for Python projects designed to be quick to set up and easy to ensure compatibility across different development environments.

## Features

This template provides:

- **Automated Environment Setup**: Streamlined virtual environment creation and dependency management
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux
- **Modern Python Packaging**: Uses `pyproject.toml` with hatchling build system
- **Testing Framework**: Pre-configured pytest setup with example tests
- **Development Tools**: Includes pylint configuration and common dependencies
- **Git Integration**: Comprehensive `.gitignore` for Python data analysis projects

## Project Structure

```
.
├── .gitignore              # Comprehensive Python .gitignore
├── pyproject.toml          # Modern Python project configuration
├── README.md               # This file
├── requirements.txt        # Project dependencies
├── setup_and_activate.sh   # Environment setup and activation script
├── src/                    # Source code directory
│   ├── __init__.py
│   ├── main.py            # Main application entry point
│   └── setup_env.py       # Environment setup automation
└── tests/                  # Test directory
    └── test_main.py       # Example test file
```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Git Bash (on Windows) or any Unix-like shell

### Setup and Activation

1. **Clone or download this template**
2. **Navigate to the project directory**
3. **Run the setup script** (must be sourced):

```bash
source ./setup_and_activate.sh
```

**Important**: The script must be sourced (not executed directly) to properly activate the virtual environment in your current shell session.

### What the Setup Script Does

The [`setup_and_activate.sh`](setup_and_activate.sh) script:

1. **Runs Environment Setup**: Executes [`src/setup_env.py`](src/setup_env.py) which:
   - Creates a virtual environment named `venv`
   - Upgrades pip to the latest version
   - Installs dependencies from [`requirements.txt`](requirements.txt)
   - Installs the `src` directory as an editable package

2. **Activates Virtual Environment**: Automatically detects your operating system and activates the virtual environment using the appropriate activation script

3. **Cross-Platform Detection**: Handles both Windows (Git Bash/MSYS) and Unix-like systems automatically

## Included Dependencies

The template includes these commonly used packages:

- **pandas**: Data manipulation and analysis
- **structlog**: Structured logging
- **pytest**: Testing framework
- **click**: Command-line interface creation
- **rich**: Rich text and beautiful formatting

## Testing

Run tests using pytest:

```bash
pytest
```

The test configuration is defined in [`pyproject.toml`](pyproject.toml) and will automatically discover tests in the `tests/` directory.

## Development

### Adding Dependencies

1. Add new dependencies to [`requirements.txt`](requirements.txt)
2. Install them in your activated environment:
   ```bash
   pip install -r requirements.txt
   ```

### Package Configuration

Modify [`pyproject.toml`](pyproject.toml) to:
- Change the package name and description
- Add or remove dependencies
- Configure build settings
- Adjust tool configurations (pytest, pylint)

## Customization

### For Data Analysis Projects

The template is optimized for data analysis with:
- Pre-configured data directories in [`.gitignore`](.gitignore) (`/data/`, `/results/`)
- Common data science packages in dependencies
- Structured logging for reproducible analysis

### For General Python Projects

Simply modify:
- [`requirements.txt`](requirements.txt) - Update dependencies
- [`pyproject.toml`](pyproject.toml) - Change project metadata
- [`src/main.py`](src/main.py) - Add your application logic

## Troubleshooting

### Script Must Be Sourced Error

If you see "This script must be sourced", run:
```bash
source ./setup_and_activate.sh
```
Instead of:
```bash
./setup_and_activate.sh  # This won't work
```

### Virtual Environment Not Found

If the virtual environment creation fails:
1. Ensure Python 3.8+ is installed
2. Check that `python` is available in your PATH
3. Run [`src/setup_env.py`](src/setup_env.py) directly: `python src/setup_env.py`

### Permission Issues (Unix-like systems)

Make the script executable:
```bash
chmod +x setup_and_activate.sh
```

## Contributing

Feel free to fork this template and customize it for your needs. Consider contributing improvements back to help others!

## License

This template is provided as-is for educational and development purposes.