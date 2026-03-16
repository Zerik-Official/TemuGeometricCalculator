def area(base: float, height: float) -> float:
    """
    Calculates the area of a triangle given its base and height.

    Formula:
        A = (b * h) / 2

    Args:
        base (float): The length of the base of the triangle.
        height (float): The perpendicular height from the base.

    Returns:
        float: The area of the triangle.
    """
    return (base * height) / 2


def area_heron(side_a: float, side_b: float, side_c: float) -> float:
    """
    Calculates the area of a triangle using Heron's formula,
    useful when all three sides are known but the height is not.

    Formula:
        s = (a + b + c) / 2
        A = sqrt(s * (s - a) * (s - b) * (s - c))

    Args:
        side_a (float): The length of the first side.
        side_b (float): The length of the second side.
        side_c (float): The length of the third side.

    Returns:
        float: The area of the triangle.
    """
    s = (side_a + side_b + side_c) / 2
    return (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5


def perimeter(side_a: float, side_b: float, side_c: float) -> float:
    """
    Calculates the perimeter of a triangle by summing all three sides.

    Formula:
        P = a + b + c

    Args:
        side_a (float): The length of the first side.
        side_b (float): The length of the second side.
        side_c (float): The length of the third side.

    Returns:
        float: The perimeter of the triangle.
    """
    return side_a + side_b + side_c


def height_from_area(area: float, base: float) -> float:
    """
    Derives the height of a triangle from its area and base.

    Formula:
        h = (2 * A) / b

    Args:
        area (float): The known area of the triangle.
        base (float): The known base of the triangle.

    Returns:
        float: The height of the triangle.
    """
    return (2 * area) / base


def base_from_area(area: float, height: float) -> float:
    """
    Derives the base of a triangle from its area and height.

    Formula:
        b = (2 * A) / h

    Args:
        area (float): The known area of the triangle.
        height (float): The known height of the triangle.

    Returns:
        float: The base of the triangle.
    """
    return (2 * area) / height


def semiperimeter(side_a: float, side_b: float, side_c: float) -> float:
    """
    Calculates the semiperimeter of a triangle, an auxiliary value
    used in Heron's formula and other calculations.

    Formula:
        s = (a + b + c) / 2

    Args:
        side_a (float): The length of the first side.
        side_b (float): The length of the second side.
        side_c (float): The length of the third side.

    Returns:
        float: The semiperimeter of the triangle.
    """
    return (side_a + side_b + side_c) / 2
