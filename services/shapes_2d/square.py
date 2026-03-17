def area(side: float) -> float:
    """
    Calculates the area of a square.

    Formula:
        A = l^2

    Args:
        side (float): The length of one side of the square. Must be greater than 0.

    Returns:
        float: The area of the square.

    Raises:
        ValueError: If side is not greater than 0.
    """
    if side <= 0:
        raise ValueError("El lado debe ser mayor que 0.")
    return side**2


def perimeter(side: float) -> float:
    """
    Calculates the perimeter of a square.

    Formula:
        P = 4 * l

    Args:
        side (float): The length of one side of the square. Must be greater than 0.

    Returns:
        float: The perimeter of the square.

    Raises:
        ValueError: If side is not greater than 0.
    """
    if side <= 0:
        raise ValueError("El lado debe ser mayor que 0.")
    return 4 * side


def side_from_area(area: float) -> float:
    """
    Derives the side length of a square from its area.

    Formula:
        l = sqrt(A)

    Args:
        area (float): The known area of the square. Must be greater than 0.

    Returns:
        float: The side length of the square.

    Raises:
        ValueError: If area is not greater than 0.
    """
    if area <= 0:
        raise ValueError("El área debe ser mayor que 0.")
    return area**0.5


def side_from_perimeter(perimeter: float) -> float:
    """
    Derives the side length of a square from its perimeter.

    Formula:
        l = P / 4

    Args:
        perimeter (float): The known perimeter of the square. Must be greater than 0.

    Returns:
        float: The side length of the square.

    Raises:
        ValueError: If perimeter is not greater than 0.
    """
    if perimeter <= 0:
        raise ValueError("El perímetro debe ser mayor que 0.")
    return perimeter / 4


def diagonal(side: float) -> float:
    """
    Calculates the diagonal of a square using the Pythagorean theorem.

    Formula:
        d = l * sqrt(2)

    Args:
        side (float): The length of one side of the square. Must be greater than 0.

    Returns:
        float: The length of the diagonal of the square.

    Raises:
        ValueError: If side is not greater than 0.
    """
    if side <= 0:
        raise ValueError("El lado debe ser mayor que 0.")
    return side * 2**0.5


def side_from_diagonal(diagonal: float) -> float:
    """
    Derives the side length of a square from its diagonal.

    Formula:
        l = d / sqrt(2)

    Args:
        diagonal (float): The known diagonal of the square. Must be greater than 0.

    Returns:
        float: The side length of the square.

    Raises:
        ValueError: If diagonal is not greater than 0.
    """
    if diagonal <= 0:
        raise ValueError("La diagonal debe ser mayor que 0.")
    return diagonal / 2**0.5
