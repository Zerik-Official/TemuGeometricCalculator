def area(base: float, height: float) -> float:
    """
    Calculates the area of a triangle given its base and height.

    Formula:
        A = (b * h) / 2

    Args:
        base (float): The length of the base of the triangle. Must be greater than 0.
        height (float): The perpendicular height from the base. Must be greater than 0.

    Returns:
        float: The area of the triangle.

    Raises:
        ValueError: If base or height is not greater than 0.
    """
    if base <= 0:
        raise ValueError("La base debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return (base * height) / 2


def area_heron(side_a: float, side_b: float, side_c: float) -> float:
    """
    Calculates the area of a triangle using Heron's formula,
    useful when all three sides are known but the height is not.

    Formula:
        s = (a + b + c) / 2
        A = sqrt(s * (s - a) * (s - b) * (s - c))

    Args:
        side_a (float): The length of the first side. Must be greater than 0.
        side_b (float): The length of the second side. Must be greater than 0.
        side_c (float): The length of the third side. Must be greater than 0.

    Returns:
        float: The area of the triangle.

    Raises:
        ValueError: If any side is not greater than 0.
        ValueError: If the three sides do not satisfy the triangle inequality.
    """
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise ValueError("Todos los lados deben ser mayores que 0.")
    if (
        side_a + side_b <= side_c
        or side_a + side_c <= side_b
        or side_b + side_c <= side_a
    ):
        raise ValueError(
            "Los lados no forman un triángulo válido (desigualdad triangular)."
        )
    s = (side_a + side_b + side_c) / 2
    return (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5


def perimeter(side_a: float, side_b: float, side_c: float) -> float:
    """
    Calculates the perimeter of a triangle by summing all three sides.

    Formula:
        P = a + b + c

    Args:
        side_a (float): The length of the first side. Must be greater than 0.
        side_b (float): The length of the second side. Must be greater than 0.
        side_c (float): The length of the third side. Must be greater than 0.

    Returns:
        float: The perimeter of the triangle.

    Raises:
        ValueError: If any side is not greater than 0.
        ValueError: If the three sides do not satisfy the triangle inequality.
    """
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise ValueError("Todos los lados deben ser mayores que 0.")
    if (
        side_a + side_b <= side_c
        or side_a + side_c <= side_b
        or side_b + side_c <= side_a
    ):
        raise ValueError(
            "Los lados no forman un triángulo válido (desigualdad triangular)."
        )
    return side_a + side_b + side_c


def height_from_area(area: float, base: float) -> float:
    """
    Derives the height of a triangle from its area and base.

    Formula:
        h = (2 * A) / b

    Args:
        area (float): The known area of the triangle. Must be greater than 0.
        base (float): The known base of the triangle. Must be greater than 0.

    Returns:
        float: The height of the triangle.

    Raises:
        ValueError: If area or base is not greater than 0.
    """
    if area <= 0:
        raise ValueError("El área debe ser mayor que 0.")
    if base <= 0:
        raise ValueError("La base debe ser mayor que 0.")
    return (2 * area) / base


def base_from_area(area: float, height: float) -> float:
    """
    Derives the base of a triangle from its area and height.

    Formula:
        b = (2 * A) / h

    Args:
        area (float): The known area of the triangle. Must be greater than 0.
        height (float): The known height of the triangle. Must be greater than 0.

    Returns:
        float: The base of the triangle.

    Raises:
        ValueError: If area or height is not greater than 0.
    """
    if area <= 0:
        raise ValueError("El área debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return (2 * area) / height


def semiperimeter(side_a: float, side_b: float, side_c: float) -> float:
    """
    Calculates the semiperimeter of a triangle, an auxiliary value
    used in Heron's formula and other calculations.

    Formula:
        s = (a + b + c) / 2

    Args:
        side_a (float): The length of the first side. Must be greater than 0.
        side_b (float): The length of the second side. Must be greater than 0.
        side_c (float): The length of the third side. Must be greater than 0.

    Returns:
        float: The semiperimeter of the triangle.

    Raises:
        ValueError: If any side is not greater than 0.
        ValueError: If the three sides do not satisfy the triangle inequality.
    """
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise ValueError("Todos los lados deben ser mayores que 0.")
    if (
        side_a + side_b <= side_c
        or side_a + side_c <= side_b
        or side_b + side_c <= side_a
    ):
        raise ValueError(
            "Los lados no forman un triángulo válido (desigualdad triangular)."
        )
    return (side_a + side_b + side_c) / 2
