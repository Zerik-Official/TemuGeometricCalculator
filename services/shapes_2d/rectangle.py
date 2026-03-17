def area(base: float, height: float) -> float:
    """
    Calculates the area of a rectangle.

    Formula:
        A = b * h

    Args:
        base (float): The length of the base of the rectangle. Must be greater than 0.
        height (float): The height of the rectangle. Must be greater than 0.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If base or height is not greater than 0.
    """
    if base <= 0:
        raise ValueError("La base debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return base * height


def perimeter(base: float, height: float) -> float:
    """
    Calculates the perimeter of a rectangle.

    Formula:
        P = 2 * (b + h)

    Args:
        base (float): The length of the base of the rectangle. Must be greater than 0.
        height (float): The height of the rectangle. Must be greater than 0.

    Returns:
        float: The perimeter of the rectangle.

    Raises:
        ValueError: If base or height is not greater than 0.
    """
    if base <= 0:
        raise ValueError("La base debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return 2 * (base + height)


def diagonal(base: float, height: float) -> float:
    """
    Calculates the diagonal of a rectangle using the Pythagorean theorem.

    Formula:
        d = sqrt(b^2 + h^2)

    Args:
        base (float): The length of the base of the rectangle. Must be greater than 0.
        height (float): The height of the rectangle. Must be greater than 0.

    Returns:
        float: The length of the diagonal of the rectangle.

    Raises:
        ValueError: If base or height is not greater than 0.
    """
    if base <= 0:
        raise ValueError("La base debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return (base**2 + height**2) ** 0.5


def height_from_area(area: float, base: float) -> float:
    """
    Derives the height of a rectangle from its area and base.

    Formula:
        h = A / b

    Args:
        area (float): The known area of the rectangle. Must be greater than 0.
        base (float): The known base of the rectangle. Must be greater than 0.

    Returns:
        float: The height of the rectangle.

    Raises:
        ValueError: If area or base is not greater than 0.
    """
    if area <= 0:
        raise ValueError("El área debe ser mayor que 0.")
    if base <= 0:
        raise ValueError("La base debe ser mayor que 0.")
    return area / base


def base_from_area(area: float, height: float) -> float:
    """
    Derives the base of a rectangle from its area and height.

    Formula:
        b = A / h

    Args:
        area (float): The known area of the rectangle. Must be greater than 0.
        height (float): The known height of the rectangle. Must be greater than 0.

    Returns:
        float: The base of the rectangle.

    Raises:
        ValueError: If area or height is not greater than 0.
    """
    if area <= 0:
        raise ValueError("El área debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return area / height


def height_from_diagonal(diagonal: float, base: float) -> float:
    """
    Derives the height of a rectangle from its diagonal and base.

    Formula:
        h = sqrt(d^2 - b^2)

    Args:
        diagonal (float): The known diagonal of the rectangle. Must be greater than 0.
        base (float): The known base of the rectangle. Must be greater than 0.

    Returns:
        float: The height of the rectangle.

    Raises:
        ValueError: If diagonal or base is not greater than 0.
        ValueError: If base is greater than or equal to diagonal (geometrically impossible).
    """
    if diagonal <= 0:
        raise ValueError("La diagonal debe ser mayor que 0.")
    if base <= 0:
        raise ValueError("La base debe ser mayor que 0.")
    if base >= diagonal:
        raise ValueError("La base debe ser menor que la diagonal.")
    return (diagonal**2 - base**2) ** 0.5
