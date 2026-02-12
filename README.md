# Mean-Variance-Standard Deviation Calculator

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Required-green.svg)](https://numpy.org/)

**freeCodeCamp Data Analysis with Python Certification - Project 1**

A Python function that calculates statistical measures (mean, variance, standard deviation, max, min, and sum) for a 3x3 matrix along different axes.

## 📋 Project Description

This project is part of the [freeCodeCamp Data Analysis with Python Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/).

The `calculate()` function takes a list of 9 numbers and:
1. Converts it to a 3×3 NumPy array
2. Calculates statistics along both axes and for the flattened matrix
3. Returns results in a dictionary format

## 🚀 Features

- ✅ Mean calculation (axis 0, axis 1, flattened)
- ✅ Variance calculation
- ✅ Standard deviation calculation
- ✅ Maximum and minimum values
- ✅ Sum of elements
- ✅ Input validation with error handling

## 📦 Installation

### Requirements
- Python 3.7 or higher
- NumPy

### Setup
```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/mean-var-std-calculator.git
cd mean-var-std-calculator

# Install dependencies
pip install numpy
```

## 💻 Usage

```python
from mean_var_std import calculate

# Example 1: Basic usage
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)

# Output:
# {
#   'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
#   'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
#   'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.581...],
#   'max': [[6, 7, 8], [2, 5, 8], 8],
#   'min': [[0, 1, 2], [0, 3, 6], 0],
#   'sum': [[9, 12, 15], [3, 12, 21], 36]
# }

# Example 2: Error handling
try:
    calculate([1, 2, 3])  # Only 3 elements
except ValueError as e:
    print(e)  # "List must contain nine numbers."
```

## 🧮 How It Works

### Input
A list of exactly 9 numbers: `[0, 1, 2, 3, 4, 5, 6, 7, 8]`

### Matrix Conversion
```
[0, 1, 2, 3, 4, 5, 6, 7, 8]  →  [[0, 1, 2],
                                  [3, 4, 5],
                                  [6, 7, 8]]
```

### Calculations

**Axis 0 (columns)** - Calculates down each column:
```
Column 1: [0, 3, 6] → mean = 3.0
Column 2: [1, 4, 7] → mean = 4.0
Column 3: [2, 5, 8] → mean = 5.0
```

**Axis 1 (rows)** - Calculates across each row:
```
Row 1: [0, 1, 2] → mean = 1.0
Row 2: [3, 4, 5] → mean = 4.0
Row 3: [6, 7, 8] → mean = 7.0
```

**Flattened** - Calculates for all elements:
```
All elements: [0,1,2,3,4,5,6,7,8] → mean = 4.0
```

## 🧪 Testing

Run the included test file:
```bash
python main.py
```

Run official freeCodeCamp tests:
```bash
python -m pytest test_module.py
```

## 📁 Project Structure

```
mean-var-std-calculator/
├── mean_var_std.py      # Main calculator function
├── main.py              # Test/demo file
├── test_module.py       # Unit tests
└── README.md            # This file
```

## 🎓 Learning Outcomes

This project demonstrates:
- NumPy array manipulation and reshaping
- Axis-based calculations in multi-dimensional arrays
- Statistical computations (mean, variance, std dev)
- Input validation and error handling
- Converting between NumPy arrays and Python lists

## 🔗 Links

- [freeCodeCamp Project Page](https://www.freecodecamp.org/learn/data-analysis-with-python/)
- [NumPy Documentation](https://numpy.org/doc/)
- [My freeCodeCamp Profile](https://www.freecodecamp.org/YOUR-USERNAME)

## 📝 License

This project is part of the freeCodeCamp curriculum and is available for educational purposes.

## 👨‍💻 Author

Your Name - [GitHub](https://github.com/YOUR-USERNAME)

---

**Note**: This is project 1 of 5 required for the Data Analysis with Python Certification.
