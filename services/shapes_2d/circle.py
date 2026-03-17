PI = 3.141592653589793

def area(radius: float) -> float:
    """
    Calculates the area of a circle.

    Formula:
        A = PI * r^2

    Args:
        radius (float): The radius of the circle. Must be greater than 0.

    Returns:
        float: The area of the circle.

    Raises:
        ValueError: If radius is not greater than 0.
    """

    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    return PI * radius**2


def perimeter(radius: float) -> float:
    """
    Calculates the perimeter (circumference) of a circle.

    Formula:
        P = 2 * PI * r

    Args:
        radius (float): The radius of the circle. Must be greater than 0.

    Returns:
        float: The perimeter of the circle.

    Raises:
        ValueError: If radius is not greater than 0.
    """

    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    return 2 * PI * radius


def radius_from_area(area: float) -> float:
    """
    Derives the radius of a circle from its area.

    Formula:
        r = sqrt(A / PI)

    Args:
        area (float): The known area of the circle. Must be greater than 0.

    Returns:
        float: The radius of the circle.

    Raises:
        ValueError: If area is not greater than 0.
    """

    if area <= 0:
        raise ValueError("El área debe ser mayor que 0.")
    return (area / PI) ** 0.5


def radius_from_perimeter(perimeter: float) -> float:
    """
    Derives the radius of a circle from its perimeter.

    Formula:
        r = P / (2 * PI)

    Args:
        perimeter (float): The known perimeter of the circle. Must be greater than 0.

    Returns:
        float: The radius of the circle.

    Raises:
        ValueError: If perimeter is not greater than 0.
    """

    if perimeter <= 0:
        raise ValueError("El perímetro debe ser mayor que 0.")
    return perimeter / (2 * PI)


def diameter(radius: float) -> float:
    """
    Calculates the diameter of a circle.

    Formula:
        d = 2 * r

    Args:
        radius (float): The radius of the circle. Must be greater than 0.

    Returns:
        float: The diameter of the circle.

    Raises:
        ValueError: If radius is not greater than 0.
    """

    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    return 2 * radius


def sector_area(radius: float, angle_degrees: float) -> float:
    """
    Calculates the area of a circular sector (pie slice).

    Formula:
        A = (angle / 360) * PI * r^2

    Args:
        radius (float): The radius of the circle. Must be greater than 0.
        angle_degrees (float): The central angle of the sector in degrees.
                               Must be greater than 0 and less than or equal to 360.

    Returns:
        float: The area of the circular sector.

    Raises:
        ValueError: If radius is not greater than 0.
        ValueError: If angle_degrees is not in the range (0, 360].
    """

    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    if angle_degrees <= 0 or angle_degrees > 360:
        raise ValueError(
            "El ángulo debe estar entre 0° (exclusivo) y 360° (inclusivo)."
        )
    return (angle_degrees / 360) * PI * radius**2
