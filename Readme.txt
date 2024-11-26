# Build and Test Instructions for CalculatorApp

## Requirements
- Python 3.x installed on Windows
- PowerShell (for zipping the files)

## Running the Build Script

1. To run tests, create a virtual environment, and package the application, use:
   ```
   build.bat
   ```

This script will generate a zip file named `calculator_app.zip` if all tests pass.

## Testing the Pipeline
Automated Trigger:
Make a small change to the repository to verify automated trigger and confirming that Jenkins starts the build automatically within 2 minutes.
