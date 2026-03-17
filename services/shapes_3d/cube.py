def volume(side: float) -> float:
    """
    Calculates the volume of a cube.

    Formula:
        V = l^3

    Args:
        side (float): The length of one edge of the cube. Must be greater than 0.

    Returns:
        float: The volume of the cube.

    Raises:
        ValueError: If side is not greater than 0.
    """
    if side <= 0:
        raise ValueError("El lado debe ser mayor que 0.")
    return side**3


def surface_area(side: float) -> float:
    """
    Calculates the total surface area of a cube (sum of its 6 faces).

    Formula:
        A = 6 * l^2

    Args:
        side (float): The length of one edge of the cube. Must be greater than 0.

    Returns:
        float: The total surface area of the cube.

    Raises:
        ValueError: If side is not greater than 0.
    """
    if side <= 0:
        raise ValueError("El lado debe ser mayor que 0.")
    return 6 * side**2


def side_from_volume(volume: float) -> float:
    """
    Derives the edge length of a cube from its volume.

    Formula:
        l = V^(1/3)

    Args:
        volume (float): The known volume of the cube. Must be greater than 0.

    Returns:
        float: The edge length of the cube.

    Raises:
        ValueError: If volume is not greater than 0.
    """
    if volume <= 0:
        raise ValueError("El volumen debe ser mayor que 0.")
    return volume ** (1 / 3)


def side_from_surface_area(surface_area: float) -> float:
    """
    Derives the edge length of a cube from its total surface area.

    Formula:
        l = sqrt(A / 6)

    Args:
        surface_area (float): The known total surface area of the cube. Must be greater than 0.

    Returns:
        float: The edge length of the cube.

    Raises:
        ValueError: If surface_area is not greater than 0.
    """
    if surface_area <= 0:
        raise ValueError("El área de superficie debe ser mayor que 0.")
    return (surface_area / 6) ** 0.5


def face_diagonal(side: float) -> float:
    """
    Calculates the diagonal of one face (square) of the cube.

    Formula:
        d_face = l * sqrt(2)

    Args:
        side (float): The length of one edge of the cube. Must be greater than 0.

    Returns:
        float: The length of the face diagonal.

    Raises:
        ValueError: If side is not greater than 0.
    """
    if side <= 0:
        raise ValueError("El lado debe ser mayor que 0.")
    return side * 2**0.5


def space_diagonal(side: float) -> float:
    """
    Calculates the space diagonal of a cube, which is the line
    connecting two opposite vertices through the interior.

    Formula:
        d = l * sqrt(3)

    Args:
        side (float): The length of one edge of the cube. Must be greater than 0.

    Returns:
        float: The length of the space diagonal of the cube.

    Raises:
        ValueError: If side is not greater than 0.
    """
    if side <= 0:
        raise ValueError("El lado debe ser mayor que 0.")
    return side * 3**0.5
