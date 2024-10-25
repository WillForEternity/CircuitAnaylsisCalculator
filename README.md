## SteadyStateCalculator.py 

This **Circuit Analysis Calculator** could also be called **Complex Square Matrix Equation Solver**, and is a Python-based tool for solving complex systems of linear equations, making it ideal for applications in fields such as electrical engineering, control systems, and signal processing. The program is designed to accept and validate complex number inputs, calculate solutions with precise complex arithmetic, and provide results in various formats including Cartesian, polar, and sinusoidal representations. This flexibility enables users to work directly with complex numbers and visualize steady-state responses or other analyses requiring matrix solutions.

## How It Works

The program employs **NumPy** to perform the core matrix calculations, including solving \( Ax = b \) for \( x \), where \( A \) is a complex square matrix and \( b \) is a complex vector. 

- **Input Validation:** Users are guided through interactive prompts to enter the matrix dimensions and values. The program ensures inputs are formatted correctly as complex numbers.
- **Matrix Conditioning:** A condition number check evaluates the matrix's stability, alerting users if the system is poorly conditioned and solutions may be inaccurate.
- **Solution Formats:**
  - **Cartesian Form:** Standard \( a + bj \) representation of complex numbers.
  - **Polar Form:** Magnitude and phase angle, which is useful for AC circuit analysis.
  - **Sinusoidal Representation:** Solutions are formatted as sinusoidal functions, reflecting time-domain behavior for steady-state analyses.

## Setup Instructions

### Prerequisites

- **Python 3.7 or higher** is required for compatibility with the code.
- **NumPy** library is needed for complex matrix operations.

### Using a Virtual Environment

To keep dependencies organized, it’s recommended to `pip install` NumPy and run the program in a virtual environment.

1. **Steps to run `SteadyStateCalculator.py`**

***Create a virtual environment in the project directory:***
```bash
python3 -m venv venv
```
***Activate the virtual environment:***
On macOS/Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```
***Install NumPy in the Virtual Environment:***
```bash
pip install numpy
```
***Run the Solver Program:***
With the environment activated, you can execute the program as follows:

```bash
python solver.py
```
But using Apple silicon, 
```bash 
python3 solver.py
```
is needed. If this is giving you errors, consult a frontier language model about the issue. Lol. 

***Deactivating the Virtual Environment***
Once you're done, you can deactivate the virtual environment with:

```bash
deactivate
```
**Example Run**

Input
```bash
(EECalcEnv) myLaptop Circuit_Analysis_Calculator % python3 SteadyStateCalculator.py

Complex-Valued Matrix Equation Solver for Steady-State Analysis
This solver accepts complex numbers in both matrix A and vector b
Use 'j' for the imaginary unit (e.g., 1+2j, 3j, 4-5j)

Enter the number of unknowns (n): 2

Enter the elements of matrix A (complex numbers allowed):
A[1][1] = 2+3j
A[1][2] = 1-j
A[2][1] = 1
A[2][2] = 0

Enter the elements of vector b (complex numbers allowed):
b[1] = 5  
b[2] = 1+3j
```

Output

```bash
Solution vector x in Cartesian form:
v1 = 1.00+3.00j
v2 = 10.50+1.50j

Solution vector x in polar form:
v1 = 3.16∠71.6°
v2 = 10.61∠8.1°

Steady-State Response Values:
v1(t) = 3.16cos(t + 71.6°)
v2(t) = 10.61cos(t + 8.1°)
```
