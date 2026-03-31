# Point Time Calculator

A simple Python Tkinter app that calculates how long it will take to reach a target number of points based on current points and recharge time.
A small project to demonstrate CI/CD workflows.

## Features
Input: Current points, needed points, and recharge time per point
Outputs:
- Hours and minutes needed to reach target
- Estimated time the points will be charged
- Simple GUI using Tkinter
- Cross-platform Python app (Windows .exe or Linux binary are generated as artifacts)

## Installation and usage
### 1. Local run
1. Install dependencies
```py
pip install -r requirements.txt
```
2. Run the app
```py
python src/pt_calc.py
```

### 2. Run the built binaries (Windows/Linux)
You can download the executables that are obtained as artifacts from the **CD workflow**
- Windows: Executbale .exe
- Linux: Binary

## Testing 
Run tests locally from the main directory:
```py
python -m pytest
```

## CI/CD
This project demonstrates basic CI/CD workflows:

- CI (.github/workflows/ci.yml) 
  1. Runs on push or pull requests to main
  2. Installs dependencies and runs tests
- CD (.github/workflows/cd.yml) 
  1. Runs on pushes to main
  2. Builds platform-specific executables (Windows .exe, Linux binary)
  3. Uploads binaries as artifacts for delivery
