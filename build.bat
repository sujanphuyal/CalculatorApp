@echo off
REM Build script for CalculatorApp

REM Create a virtual environment and install dependencies if required
echo Initializing virtual environment...
python -m venv venv
call venv\Scripts\activate
if exist requirements.txt (
    pip install -r requirements.txt
)

REM Run the unit tests
echo Running tests...
python -m unittest test_calculator.py
if %errorlevel% neq 0 (
    echo Some tests failed. Exiting build process.
    exit /b 1
)

REM Create a deployable package (zip file)
echo Packaging application...
mkdir calculator_app
copy calculator.py calculator_app\
copy test_calculator.py calculator_app\
copy README.md calculator_app\
powershell Compress-Archive -Path calculator_app\* -DestinationPath calculator_app.zip
rmdir /S /Q calculator_app

echo Build and packaging complete.
