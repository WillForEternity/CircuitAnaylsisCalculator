import numpy as np
from typing import Tuple, List
import cmath

def get_complex_input(prompt: str) -> complex:
    """Get and validate complex number input from user."""
    while True:
        try:
            value = input(prompt)
            if not value.strip():
                print("Input cannot be empty. Please enter a complex number.")
                continue
            
            value = value.replace('i', 'j')
            value = value.replace('+j', '+1j').replace('-j', '-1j')
            if value.startswith('j'):
                value = '1' + value
                
            result = complex(eval(value))
            
            if not (np.isfinite(result.real) and np.isfinite(result.imag)):
                raise ValueError("Result contains infinity or NaN")
                
            return result
        except Exception as e:
            print(f"Invalid input. Please enter a valid complex number using 'j' for the imaginary part.")
            print(f"Example formats: 1+2j, 3-4j, 5j, 6")

def format_complex(num: complex, tolerance: float = 1e-12) -> str:
    """Format complex number with appropriate precision for circuit analysis."""
    # Clean small values
    real = 0.0 if abs(num.real) < tolerance else num.real
    imag = 0.0 if abs(num.imag) < tolerance else num.imag
    
    # Format with 2 decimal places
    if abs(real) < tolerance and abs(imag) < tolerance:
        return "0"
    elif abs(real) < tolerance:
        return f"{imag:.2f}j"
    elif abs(imag) < tolerance:
        return f"{real:.2f}"
    else:
        imag_str = f"+{imag:.2f}j" if imag >= 0 else f"{imag:.2f}j"
        return f"{real:.2f}{imag_str}"

def format_polar(magnitude: float, angle_deg: float) -> str:
    """Format complex number in polar form."""
    if abs(magnitude) < 1e-12:
        return "0"
    return f"{magnitude:.2f}∠{angle_deg:.1f}°"

def format_sinusoidal(magnitude: float, angle_deg: float) -> str:
    """Format complex number as sinusoidal function."""
    if abs(magnitude) < 1e-12:
        return "0"
        
    if abs(angle_deg) < 0.1:
        return f"{magnitude:.2f}cos(t)"
    elif angle_deg <= 180:
        return f"{magnitude:.2f}cos(t + {angle_deg:.1f}°)"
    else:
        return f"{magnitude:.2f}cos(t - {360 - angle_deg:.1f}°)"

def solve_complex_system(A: np.ndarray, b: np.ndarray) -> Tuple[List[complex], List[Tuple[float, float]]]:
    """Solve the complex system and return solutions in both cartesian and polar forms."""
    condition_number = np.linalg.cond(A)
    if condition_number > 1e12:
        print(f"\nWarning: Matrix is poorly conditioned (condition number: {condition_number:.2e})")
        print("Results may be inaccurate. Consider reviewing your system of equations.")
    
    x = np.linalg.solve(A, b)
    
    polar_forms = []
    for val in x:
        magnitude = abs(val)
        angle = np.degrees(cmath.phase(val)) % 360
        polar_forms.append((magnitude, angle))
    
    return x, polar_forms

def main():
    print("\nComplex-Valued Matrix Equation Solver for Steady-State Analysis")
    print("This solver accepts complex numbers in both matrix A and vector b")
    print("Use 'j' for the imaginary unit (e.g., 1+2j, 3j, 4-5j)\n")
    
    while True:
        try:
            n = int(input("Enter the number of unknowns (n): "))
            if n <= 0:
                raise ValueError("Number of unknowns must be positive")
            break
        except ValueError as e:
            print(f"Invalid input: {str(e)}")
    
    A = np.zeros((n, n), dtype=complex)
    b = np.zeros(n, dtype=complex)
    
    print("\nEnter the elements of matrix A (complex numbers allowed):")
    for i in range(n):
        for j in range(n):
            A[i][j] = get_complex_input(f"A[{i+1}][{j+1}] = ")
    
    print("\nEnter the elements of vector b (complex numbers allowed):")
    for i in range(n):
        b[i] = get_complex_input(f"b[{i+1}] = ")
    
    try:
        x_cartesian, x_polar = solve_complex_system(A, b)
        
        print("\nSolution vector x in Cartesian form:")
        for i, val in enumerate(x_cartesian):
            print(f"v{i+1} = {format_complex(val)}")
        
        print("\nSolution vector x in polar form:")
        for i, (magnitude, angle) in enumerate(x_polar):
            print(f"v{i+1} = {format_polar(magnitude, angle)}")
        
        print("\nSteady-State Response Values:")
        for i, (magnitude, angle) in enumerate(x_polar):
            print(f"v{i+1}(t) = {format_sinusoidal(magnitude, angle)}")
            
    except np.linalg.LinAlgError as e:
        print(f"\nError: Could not solve system - {str(e)}")
        print("The system may be singular or nearly singular.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
