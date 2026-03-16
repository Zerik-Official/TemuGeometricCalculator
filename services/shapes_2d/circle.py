PI = 3.141592653589793


def area(radius: float) -> float:
    """
    Calculates the area of a circle.

    Formula:
        A = PI * r^2

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return PI * radius ** 2


def perimeter(radius: float) -> float:
    """
    Calculates the perimeter (circumference) of a circle.

    Formula:
        P = 2 * PI * r

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The perimeter of the circle.
    """
    return 2 * PI * radius


def radius_from_area(area: float) -> float:
    """
    Derives the radius of a circle from its area.

    Formula:
        r = sqrt(A / PI)

    Args:
        area (float): The known area of the circle.

    Returns:
        float: The radius of the circle.
    """
    return (area / PI) ** 0.5


def radius_from_perimeter(perimeter: float) -> float:
    """
    Derives the radius of a circle from its perimeter.

    Formula:
        r = P / (2 * PI)

    Args:
        perimeter (float): The known perimeter of the circle.

    Returns:
        float: The radius of the circle.
    """
    return perimeter / (2 * PI)


def diameter(radius: float) -> float:
    """
    Calculates the diameter of a circle.

    Formula:
        d = 2 * r

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The diameter of the circle.
    """
    return 2 * radius


def sector_area(radius: float, angle_degrees: float) -> float:
    """
    Calculates the area of a circular sector (pie slice).

    Formula:
        A = (angle / 360) * PI * r^2

    Args:
        radius (float): The radius of the circle.
        angle_degrees (float): The central angle of the sector in degrees.

    Returns:
        float: The area of the circular sector.
    """
    return (angle_degrees / 360) * PI * radius ** 2
