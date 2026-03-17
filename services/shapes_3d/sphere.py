PI = 3.141592653589793


def volume(radius: float) -> float:
    """
    Calculates the volume of a sphere.

    Formula:
        V = (4/3) * PI * r^3

    Args:
        radius (float): The radius of the sphere. Must be greater than 0.

    Returns:
        float: The volume of the sphere.

    Raises:
        ValueError: If radius is not greater than 0.
    """
    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    return (4 / 3) * PI * radius**3


def surface_area(radius: float) -> float:
    """
    Calculates the surface area of a sphere.

    Formula:
        A = 4 * PI * r^2

    Args:
        radius (float): The radius of the sphere. Must be greater than 0.

    Returns:
        float: The surface area of the sphere.

    Raises:
        ValueError: If radius is not greater than 0.
    """
    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    return 4 * PI * radius**2


def radius_from_volume(volume: float) -> float:
    """
    Derives the radius of a sphere from its volume.

    Formula:
        r = ((3 * V) / (4 * PI))^(1/3)

    Args:
        volume (float): The known volume of the sphere. Must be greater than 0.

    Returns:
        float: The radius of the sphere.

    Raises:
        ValueError: If volume is not greater than 0.
    """
    if volume <= 0:
        raise ValueError("El volumen debe ser mayor que 0.")
    return ((3 * volume) / (4 * PI)) ** (1 / 3)


def radius_from_surface_area(surface_area: float) -> float:
    """
    Derives the radius of a sphere from its surface area.

    Formula:
        r = sqrt(A / (4 * PI))

    Args:
        surface_area (float): The known surface area of the sphere. Must be greater than 0.

    Returns:
        float: The radius of the sphere.

    Raises:
        ValueError: If surface_area is not greater than 0.
    """
    if surface_area <= 0:
        raise ValueError("El área de superficie debe ser mayor que 0.")
    return (surface_area / (4 * PI)) ** 0.5


def diameter(radius: float) -> float:
    """
    Calculates the diameter of a sphere.

    Formula:
        d = 2 * r

    Args:
        radius (float): The radius of the sphere. Must be greater than 0.

    Returns:
        float: The diameter of the sphere.

    Raises:
        ValueError: If radius is not greater than 0.
    """
    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    return 2 * radius


def spherical_cap_volume(radius: float, cap_height: float) -> float:
    """
    Calculates the volume of a spherical cap, which is the portion
    of a sphere cut off by a plane.

    Formula:
        V = PI * h^2 * (r - h/3)

    Args:
        radius (float): The radius of the full sphere. Must be greater than 0.
        cap_height (float): The height of the cap from the cutting plane to the pole.
                            Must be greater than 0 and less than or equal to the diameter (2 * radius).

    Returns:
        float: The volume of the spherical cap.

    Raises:
        ValueError: If radius is not greater than 0.
        ValueError: If cap_height is not in the range (0, 2 * radius].
    """
    if radius <= 0:
        raise ValueError("El radio debe ser mayor que 0.")
    if cap_height <= 0:
        raise ValueError("La altura del casquete debe ser mayor que 0.")
    if cap_height > 2 * radius:
        raise ValueError(
            "La altura del casquete no puede ser mayor que el diámetro de la esfera "
            f"(máximo: {2 * radius})."
        )
    return PI * cap_height**2 * (radius - cap_height / 3)
