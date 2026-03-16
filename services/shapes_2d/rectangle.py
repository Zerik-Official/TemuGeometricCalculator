def area(base: float, height: float) -> float:
    """
    Calculates the area of a rectangle.

    Formula:
        A = b * h

    Args:
        base (float): The length of the base of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return base * height


def perimeter(base: float, height: float) -> float:
    """
    Calculates the perimeter of a rectangle.

    Formula:
        P = 2 * (b + h)

    Args:
        base (float): The length of the base of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    return 2 * (base + height)


def diagonal(base: float, height: float) -> float:
    """
    Calculates the diagonal of a rectangle using the Pythagorean theorem.

    Formula:
        d = sqrt(b^2 + h^2)

    Args:
        base (float): The length of the base of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The length of the diagonal of the rectangle.
    """
    return (base ** 2 + height ** 2) ** 0.5


def height_from_area(area: float, base: float) -> float:
    """
    Derives the height of a rectangle from its area and base.

    Formula:
        h = A / b

    Args:
        area (float): The known area of the rectangle.
        base (float): The known base of the rectangle.

    Returns:
        float: The height of the rectangle.
    """
    return area / base


def base_from_area(area: float, height: float) -> float:
    """
    Derives the base of a rectangle from its area and height.

    Formula:
        b = A / h

    Args:
        area (float): The known area of the rectangle.
        height (float): The known height of the rectangle.

    Returns:
        float: The base of the rectangle.
    """
    return area / height


def height_from_diagonal(diagonal: float, base: float) -> float:
    """
    Derives the height of a rectangle from its diagonal and base.

    Formula:
        h = sqrt(d^2 - b^2)

    Args:
        diagonal (float): The known diagonal of the rectangle.
        base (float): The known base of the rectangle.

    Returns:
        float: The height of the rectangle.
    """
    return (diagonal ** 2 - base ** 2) ** 0.5