# Gram-Schmidt Orthogonalization

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

A Python implementation of the Gram-Schmidt process to convert a matrix into an orthogonal matrix.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Blackpanther-007/Mathematics/tree/master/Linear_algebra/Orthogonality

2. Make new branch

## Usage
    import numpy as np
    from gram_schmidt import gram_schmidt

### Create a matrix
    A = np.array([[1, 2], [3, 4]], dtype=float)

### Get orthogonal matrix
    Q = gram_schmidt(A)

    print("Original matrix:\n", A)
    print("\nOrthogonalized matrix:\n", Q)

## Basic Usage
    A = np.array([[1, 1], [1, -1]])
    Q = gram_schmidt(A)
    print(Q.T @ Q)  # ≈ Identity matrix

## Handling Linear Dependence
    try:
        A = np.array([[1, 2], [2, 4]])  # Dependent columns
        Q = gram_schmidt(A)
    except ValueError as e:
        print(f"Error: {e}")

# Documentation
## Function
    gram_schmidt(
        A: np.ndarray,
        normalize: bool = True,
        tol: float = 1e-10
    ) -> np.ndarray

   * A: Input matrix (m×n)

   * normalize: Return orthonormal columns if True

   * tol: Tolerance for linear dependence check

# Contributing
* Fork the repository

* Create your feature branch (git checkout -b feature/amazing-feature)

* Commit changes (git commit -m 'Add feature')

* Push (git push origin feature/amazing-feature)

* Open a Pull Request


## License
This repository is [MIT Licensed](LICENSE). Feel free to use these math implementations however you want!