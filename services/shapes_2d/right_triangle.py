PI = 3.141592653589793


def hypotenuse(leg_a: float, leg_b: float) -> float:
    """
    Calculates the hypotenuse of a right triangle using the Pythagorean theorem.

    Formula:
        c = sqrt(a^2 + b^2)

    Args:
        leg_a (float): The length of the first leg.
        leg_b (float): The length of the second leg.

    Returns:
        float: The length of the hypotenuse.
    """
    return (leg_a ** 2 + leg_b ** 2) ** 0.5


def leg(hypotenuse: float, known_leg: float) -> float:
    """
    Derives the unknown leg of a right triangle from the hypotenuse
    and the other known leg.

    Formula:
        a = sqrt(c^2 - b^2)

    Args:
        hypotenuse (float): The length of the hypotenuse.
        known_leg (float): The length of the known leg.

    Returns:
        float: The length of the unknown leg.
    """
    return (hypotenuse ** 2 - known_leg ** 2) ** 0.5


def area(leg_a: float, leg_b: float) -> float:
    """
    Calculates the area of a right triangle. The two legs act as
    base and height since they are perpendicular to each other.

    Formula:
        A = (a * b) / 2

    Args:
        leg_a (float): The length of the first leg.
        leg_b (float): The length of the second leg.

    Returns:
        float: The area of the right triangle.
    """
    return (leg_a * leg_b) / 2


def perimeter(leg_a: float, leg_b: float) -> float:
    """
    Calculates the perimeter of a right triangle by summing both legs
    and the hypotenuse derived from the Pythagorean theorem.

    Formula:
        P = a + b + sqrt(a^2 + b^2)

    Args:
        leg_a (float): The length of the first leg.
        leg_b (float): The length of the second leg.

    Returns:
        float: The perimeter of the right triangle.
    """
    c = (leg_a ** 2 + leg_b ** 2) ** 0.5
    return leg_a + leg_b + c


def angle_from_legs(opposite_leg: float, adjacent_leg: float) -> float:
    """
    Calculates an interior angle in degrees using the arctangent,
    given the opposite and adjacent legs relative to that angle.

    Formula:
        angle = arctan(opposite / adjacent)

    Note:
        arctan is approximated using a Taylor series expansion.

    Args:
        opposite_leg (float): The leg opposite to the angle being calculated.
        adjacent_leg (float): The leg adjacent to the angle being calculated.

    Returns:
        float: The angle in degrees.
    """
    x = opposite_leg / adjacent_leg
    sign = 1 if x >= 0 else -1
    x = abs(x)

    if x > 1:
        result = PI / 2 - _arctan_taylor(1 / x)
    else:
        result = _arctan_taylor(x)

    return sign * result * (180 / PI)


def leg_from_hypotenuse_angle(hypotenuse: float, angle_degrees: float) -> float:
    """
    Derives the leg opposite to a given angle using the sine relationship,
    given the hypotenuse and the angle opposite to the desired leg.

    Formula:
        a = c * sin(angle)

    Note:
        sin is approximated using a Taylor series expansion.

    Args:
        hypotenuse (float): The length of the hypotenuse.
        angle_degrees (float): The angle in degrees opposite to the desired leg.

    Returns:
        float: The length of the leg opposite to the given angle.
    """
    angle_rad = angle_degrees * (PI / 180)
    return hypotenuse * _sin_taylor(angle_rad)


def _arctan_taylor(x: float) -> float:
    """
    Approximates arctan(x) for |x| <= 1 using a Taylor series.

    Formula:
        arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...

    Args:
        x (float): Input value where |x| <= 1.

    Returns:
        float: Approximation of arctan(x) in radians.
    """
    result = 0.0
    power = x
    for n in range(50):
        result += ((-1) ** n) * (power / (2 * n + 1))
        power *= x * x
    return result


def _sin_taylor(x: float) -> float:
    """
    Approximates sin(x) using a Taylor series.

    Formula:
        sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...

    Args:
        x (float): Angle in radians.

    Returns:
        float: Approximation of sin(x).
    """
    result = 0.0
    term = x
    for n in range(1, 20):
        result += term
        term *= -x * x / ((2 * n) * (2 * n + 1))
    return result