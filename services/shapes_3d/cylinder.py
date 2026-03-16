PI = 3.141592653589793


def volume(radius: float, height: float) -> float:
    """
    Calculates the volume of a cylinder.

    Formula:
        V = PI * r^2 * h

    Args:
        radius (float): The radius of the circular base.
        height (float): The height of the cylinder.

    Returns:
        float: The volume of the cylinder.
    """
    return PI * radius ** 2 * height


def surface_area(radius: float, height: float) -> float:
    """
    Calculates the total surface area of a cylinder,
    including both circular bases and the lateral surface.

    Formula:
        A = 2 * PI * r * (r + h)

    Args:
        radius (float): The radius of the circular base.
        height (float): The height of the cylinder.

    Returns:
        float: The total surface area of the cylinder.
    """
    return 2 * PI * radius * (radius + height)


def lateral_area(radius: float, height: float) -> float:
    """
    Calculates the lateral surface area of a cylinder,
    excluding both bases. Equivalent to unrolling the cylinder into a rectangle.

    Formula:
        A_lat = 2 * PI * r * h

    Args:
        radius (float): The radius of the circular base.
        height (float): The height of the cylinder.

    Returns:
        float: The lateral surface area of the cylinder.
    """
    return 2 * PI * radius * height


def radius_from_volume(volume: float, height: float) -> float:
    """
    Derives the radius of a cylinder from its volume and height.

    Formula:
        r = sqrt(V / (PI * h))

    Args:
        volume (float): The known volume of the cylinder.
        height (float): The known height of the cylinder.

    Returns:
        float: The radius of the cylinder.
    """
    return (volume / (PI * height)) ** 0.5


def height_from_volume(volume: float, radius: float) -> float:
    """
    Derives the height of a cylinder from its volume and radius.

    Formula:
        h = V / (PI * r^2)

    Args:
        volume (float): The known volume of the cylinder.
        radius (float): The known radius of the cylinder.

    Returns:
        float: The height of the cylinder.
    """
    return volume / (PI * radius ** 2)
