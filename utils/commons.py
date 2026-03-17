
def param_label_with_unit(param: str) -> str:
    """
    Returns the parameter label with its unit in parentheses,
    according to the active unit system.
    Angles do not have an extra unit because they already say 'degrees'.

    Args:
        param (str): Internal parameter name.

    Returns:
        str: Parameter label with unit (e.g., "Radius (ft)") or without it for angles.
    """

    from .geometry_data import PARAM_LABELS, PARAM_TYPE

    label = PARAM_LABELS.get(param, param)
    measure_type = PARAM_TYPE.get(param, "length")
    if measure_type == "angle":
        return label
    suffix = unit_suffix(measure_type)
    return f"{label} ({suffix})"

def unit_suffix(measure_type: str) -> str:
    """
    Returns the unit suffix corresponding to the measurement type
    and the active unit system.

    Args:
        measure_type (str): "length", "area", "volume" o "angle".

    Returns:
        str: Unit suffix (e.g., "m", "ft²", "m³", "°").
    """

    from .geometry_data import unit_system

    if measure_type == "angle":
        return "°"
    if unit_system == "metric":
        return {"length": "m", "area": "m²", "volume": "m³"}.get(measure_type, "")
    return {"length": "ft", "area": "ft²", "volume": "ft³"}.get(measure_type, "")


def to_metric(value: float, measure_type: str) -> float:
    """
    Converts a value entered in the imperial system to metric
    so that internal calculations are consistent.
    If the active system is metric, returns the value without changes.

    Args:
        value (float): Value entered by the user.
        measure_type (str): "length", "area", "volume" or "angle".

    Returns:
        float: Value in metric units.
    """

    from .geometry_data import unit_system, FT2_TO_M2, FT3_TO_M3, FT_TO_M

    if unit_system == "metric" or measure_type == "angle":
        return value
    factors = {"length": FT_TO_M, "area": FT2_TO_M2, "volume": FT3_TO_M3}
    return value * factors.get(measure_type, 1.0)


def to_display(value: float, measure_type: str) -> float:
    """
    Converts a metric result to the active unit system
    for display to the user.
    If the active system is metric, returns the value without changes.

    Args:
        value (float): Result in metric units.
        measure_type (str): "length", "area", "volume" or "angle".

    Returns:
        float: Value in the active unit system.
    """
    
    from .geometry_data import unit_system, M_TO_FT, M2_TO_FT2, M3_TO_FT3

    if unit_system == "metric" or measure_type == "angle":
        return value
    factors = {"length": M_TO_FT, "area": M2_TO_FT2, "volume": M3_TO_FT3}
    return value * factors.get(measure_type, 1.0)