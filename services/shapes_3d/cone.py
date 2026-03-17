PI = 3.141592653589793

def volume(radius: float, height: float) -> float:
    """
    Calculates the volume of a cone.

    Formula:
        V = (1/3) * PI * r^2 * h

    Args:
        radius (float): The radius of the circular base. Must be greater than 0.
        height (float): The perpendicular height from the base to the apex.
                        Must be greater than 0.

    Returns:
        float: The volume of the cone.

    Raises:
        ValueError: If radius or height is not greater than 0.
    """

    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return (1 / 3) * PI * radius**2 * height


def surface_area(radius: float, height: float) -> float:
    """
    Calculates the total surface area of a cone by summing
    the circular base and the lateral surface using the slant height.

    Formula:
        g = sqrt(r^2 + h^2)
        A = PI * r * (r + g)

    Args:
        radius (float): The radius of the circular base. Must be greater than 0.
        height (float): The perpendicular height of the cone. Must be greater than 0.

    Returns:
        float: The total surface area of the cone.

    Raises:
        ValueError: If radius or height is not greater than 0.
    """

    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    g = (radius**2 + height**2) ** 0.5
    return PI * radius * (radius + g)


def lateral_area(radius: float, height: float) -> float:
    """
    Calculates the lateral surface area of a cone (excluding the base),
    using the slant height as the inclined distance from base to apex.

    Formula:
        g = sqrt(r^2 + h^2)
        A_lat = PI * r * g

    Args:
        radius (float): The radius of the circular base. Must be greater than 0.
        height (float): The perpendicular height of the cone. Must be greater than 0.

    Returns:
        float: The lateral surface area of the cone.

    Raises:
        ValueError: If radius or height is not greater than 0.
    """

    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    g = (radius**2 + height**2) ** 0.5
    return PI * radius * g


def slant_height(radius: float, height: float) -> float:
    """
    Calculates the slant height of a cone, which is the distance
    from any point on the base edge to the apex along the lateral surface.

    Formula:
        g = sqrt(r^2 + h^2)

    Args:
        radius (float): The radius of the circular base. Must be greater than 0.
        height (float): The perpendicular height of the cone. Must be greater than 0.

    Returns:
        float: The slant height of the cone.

    Raises:
        ValueError: If radius or height is not greater than 0.
    """

    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return (radius**2 + height**2) ** 0.5


def radius_from_volume(volume: float, height: float) -> float:
    """
    Derives the base radius of a cone from its volume and height.

    Formula:
        r = sqrt((3 * V) / (PI * h))

    Args:
        volume (float): The known volume of the cone. Must be greater than 0.
        height (float): The known height of the cone. Must be greater than 0.

    Returns:
        float: The base radius of the cone.

    Raises:
        ValueError: If volume or height is not greater than 0.
    """

    if volume <= 0:
        raise ValueError("El volumen debe ser mayor que 0.")
    if height <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return ((3 * volume) / (PI * height)) ** 0.5


def height_from_volume(volume: float, radius: float) -> float:
    """
    Derives the height of a cone from its volume and base radius.

    Formula:
        h = (3 * V) / (PI * r^2)

    Args:
        volume (float): The known volume of the cone. Must be greater than 0.
        radius (float): The known base radius of the cone. Must be greater than 0.

    Returns:
        float: The height of the cone.

    Raises:
        ValueError: If volume or radius is not greater than 0.
    """

    if volume <= 0:
        raise ValueError("El volumen debe ser mayor que 0.")
    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    return (3 * volume) / (PI * radius**2)
