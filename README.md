# Temu Geometric Calculator

<p align="center">
  <img src="images/temu.png" width="400">
</p>

A desktop application built with Python and CustomTkinter that calculates geometric formulas for 2D and 3D figures. The interface guides the user through selecting a figure, choosing a formula, entering values, and displaying the result.

---

## Project Structure

```
geometric_calculator/
├── main.py
├── requirements.txt
├── temu.ico
└── services/
    ├── __init__.py
    ├── shapes_2d/
    │   ├── __init__.py
    │   ├── circle.py
    │   ├── square.py
    │   ├── rectangle.py
    │   ├── triangle.py
    │   └── right_triangle.py
    └── shapes_3d/
        ├── __init__.py
        ├── sphere.py
        ├── cube.py
        ├── cylinder.py
        └── cone.py
```

Each file under `shapes_2d` and `shapes_3d` contains pure functions for a single figure. No external libraries are used in the math logic — `PI` is declared as a constant and all roots are computed with exponentiation (`** 0.5`, `** (1/3)`).

The `__init__.py` files re-export every function from their respective modules so `main.py` can import everything from a single path.

---

## Figures and Formulas

**2D:** Circle, Square, Rectangle, Triangle, Right Triangle.

**3D:** Sphere, Cube, Cylinder, Cone.

Each figure has between 5 and 6 formulas, including direct calculations (area, volume, perimeter) and inverse ones that derive an unknown parameter from a known result (e.g. radius from area, side from volume).

---

## Requirements

- Python 3.10 or higher
- CustomTkinter

All dependencies are listed in `requirements.txt`.

---

## Setup

**1. Clone the repository**

```bash
git clone <repository-url>
cd geometric_calculator
```

**2. Create and activate a virtual environment**

On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python main.py
```

or

```bash
python3 main.py
```

---

> Version 1.0

> The application is in Spanish, but the code is fully commented in English for clarity.