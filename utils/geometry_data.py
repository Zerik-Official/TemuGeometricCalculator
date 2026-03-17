from services.shapes_2d import (
    circle_area,
    circle_perimeter,
    radius_from_area,
    radius_from_perimeter,
    circle_diameter,
    sector_area,
    square_area,
    square_perimeter,
    square_diagonal,
    side_from_area,
    side_from_perimeter,
    side_from_diagonal,
    rect_area,
    rect_perimeter,
    rect_diagonal,
    height_from_area,
    base_from_area,
    height_from_diagonal,
    tri_area,
    area_heron,
    tri_perimeter,
    tri_height_from_area,
    tri_base_from_area,
    semiperimeter,
    hypotenuse,
    leg,
    rt_area,
    rt_perimeter,
    angle_from_legs,
    leg_from_hypotenuse_angle,
)

from services.shapes_3d import (
    sphere_volume,
    sphere_surface,
    sphere_r_from_vol,
    sphere_r_from_surface,
    sphere_diameter,
    spherical_cap_volume,
    cube_volume,
    cube_surface,
    face_diagonal,
    space_diagonal,
    cube_side_from_vol,
    cube_side_from_surface,
    cyl_volume,
    cyl_surface,
    cyl_lateral,
    cyl_r_from_vol,
    cyl_h_from_vol,
    cone_volume,
    cone_surface,
    cone_lateral,
    slant_height,
    cone_r_from_vol,
    cone_h_from_vol,
)

from typing import List, Dict, Any

# Global state of the system of units. "metric" or "imperial".
unit_system: str = "metric"

# Conversion factors from meters to feet for each measurement type.
# Internal calculations always work in meters (or pure metric units).
# When displaying imperial results, we multiply by these factors.

M_TO_FT: float = 3.28084  # length:  1 m  = 3.28084 ft
M2_TO_FT2: float = 10.7639  # area:      1 m² = 10.7639 ft²
M3_TO_FT3: float = 35.3147  # volume:   1 m³ = 35.3147 ft³
FT_TO_M: float = 1 / M_TO_FT
FT2_TO_M2: float = 1 / M2_TO_FT2
FT3_TO_M3: float = 1 / M3_TO_FT3

RESULT_TYPE: Dict[str, str] = {

    # Circle
    "circle_area": "area",
    "circle_perimeter": "length",
    "radius_from_area": "length",
    "radius_from_perimeter": "length",
    "circle_diameter": "length",
    "sector_area": "area",

    # Square
    "square_area": "area",
    "square_perimeter": "length",
    "square_diagonal": "length",
    "side_from_area": "length",
    "side_from_perimeter": "length",
    "side_from_diagonal": "length",

    # Rectangle
    "rect_area": "area",
    "rect_perimeter": "length",
    "rect_diagonal": "length",
    "height_from_area": "length",
    "base_from_area": "length",
    "height_from_diagonal": "length",

    # Triangle
    "tri_area": "area",
    "area_heron": "area",
    "tri_perimeter": "length",
    "tri_height_from_area": "length",
    "tri_base_from_area": "length",
    "semiperimeter": "length",

    # Right Triangle
    "hypotenuse": "length",
    "leg": "length",
    "rt_area": "area",
    "rt_perimeter": "length",
    "angle_from_legs": "angle",
    "leg_from_hypotenuse_angle": "length",

    # Sphere
    "sphere_volume": "volume",
    "sphere_surface": "area",
    "sphere_r_from_vol": "length",
    "sphere_r_from_surface": "length",
    "sphere_diameter": "length",
    "spherical_cap_volume": "volume",

    # Cube
    "cube_volume": "volume",
    "cube_surface": "area",
    "face_diagonal": "length",
    "space_diagonal": "length",
    "cube_side_from_vol": "length",
    "cube_side_from_surface": "length",

    # Cylinder
    "cyl_volume": "volume",
    "cyl_surface": "area",
    "cyl_lateral": "area",
    "cyl_r_from_vol": "length",
    "cyl_h_from_vol": "length",

    # Cone
    "cone_volume": "volume",
    "cone_surface": "area",
    "cone_lateral": "area",
    "slant_height": "length",
    "cone_r_from_vol": "length",
    "cone_h_from_vol": "length",
}

# Type of measure that each input parameter represents.
PARAM_TYPE: Dict[str, str] = {
    "radius": "length",
    "area": "area",
    "perimeter": "length",
    "angle_degrees": "angle",
    "side": "length",
    "diagonal": "length",
    "base": "length",
    "height": "length",
    "side_a": "length",
    "side_b": "length",
    "side_c": "length",
    "hypotenuse": "length",
    "known_leg": "length",
    "leg_a": "length",
    "leg_b": "length",
    "opposite_leg": "length",
    "adjacent_leg": "length",
    "surface_area": "area",
    "cap_height": "length",
    "volume": "volume",
}

# Data structure that defines the figures, formulas, parameters, and associated functions.
FIGURES: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
    "2D": {
        "Círculo": [
            {
                "label": "Área",
                "fn": circle_area,
                "fn_name": "circle_area",
                "params": ["radius"],
            },
            {
                "label": "Perímetro",
                "fn": circle_perimeter,
                "fn_name": "circle_perimeter",
                "params": ["radius"],
            },
            {
                "label": "Radio desde área",
                "fn": radius_from_area,
                "fn_name": "radius_from_area",
                "params": ["area"],
            },
            {
                "label": "Radio desde perímetro",
                "fn": radius_from_perimeter,
                "fn_name": "radius_from_perimeter",
                "params": ["perimeter"],
            },
            {
                "label": "Diámetro",
                "fn": circle_diameter,
                "fn_name": "circle_diameter",
                "params": ["radius"],
            },
            {
                "label": "Área de sector",
                "fn": sector_area,
                "fn_name": "sector_area",
                "params": ["radius", "angle_degrees"],
            },
        ],
        "Cuadrado": [
            {
                "label": "Área",
                "fn": square_area,
                "fn_name": "square_area",
                "params": ["side"],
            },
            {
                "label": "Perímetro",
                "fn": square_perimeter,
                "fn_name": "square_perimeter",
                "params": ["side"],
            },
            {
                "label": "Diagonal",
                "fn": square_diagonal,
                "fn_name": "square_diagonal",
                "params": ["side"],
            },
            {
                "label": "Lado desde área",
                "fn": side_from_area,
                "fn_name": "side_from_area",
                "params": ["area"],
            },
            {
                "label": "Lado desde perímetro",
                "fn": side_from_perimeter,
                "fn_name": "side_from_perimeter",
                "params": ["perimeter"],
            },
            {
                "label": "Lado desde diagonal",
                "fn": side_from_diagonal,
                "fn_name": "side_from_diagonal",
                "params": ["diagonal"],
            },
        ],
        "Rectángulo": [
            {
                "label": "Área",
                "fn": rect_area,
                "fn_name": "rect_area",
                "params": ["base", "height"],
            },
            {
                "label": "Perímetro",
                "fn": rect_perimeter,
                "fn_name": "rect_perimeter",
                "params": ["base", "height"],
            },
            {
                "label": "Diagonal",
                "fn": rect_diagonal,
                "fn_name": "rect_diagonal",
                "params": ["base", "height"],
            },
            {
                "label": "Altura desde área",
                "fn": height_from_area,
                "fn_name": "height_from_area",
                "params": ["area", "base"],
            },
            {
                "label": "Base desde área",
                "fn": base_from_area,
                "fn_name": "base_from_area",
                "params": ["area", "height"],
            },
            {
                "label": "Altura desde diagonal",
                "fn": height_from_diagonal,
                "fn_name": "height_from_diagonal",
                "params": ["diagonal", "base"],
            },
        ],
        "Triángulo": [
            {
                "label": "Área",
                "fn": tri_area,
                "fn_name": "tri_area",
                "params": ["base", "height"],
            },
            {
                "label": "Área (Herón)",
                "fn": area_heron,
                "fn_name": "area_heron",
                "params": ["side_a", "side_b", "side_c"],
            },
            {
                "label": "Perímetro",
                "fn": tri_perimeter,
                "fn_name": "tri_perimeter",
                "params": ["side_a", "side_b", "side_c"],
            },
            {
                "label": "Altura desde área",
                "fn": tri_height_from_area,
                "fn_name": "tri_height_from_area",
                "params": ["area", "base"],
            },
            {
                "label": "Base desde área",
                "fn": tri_base_from_area,
                "fn_name": "tri_base_from_area",
                "params": ["area", "height"],
            },
            {
                "label": "Semiperímetro",
                "fn": semiperimeter,
                "fn_name": "semiperimeter",
                "params": ["side_a", "side_b", "side_c"],
            },
        ],
        "Triángulo Rectángulo": [
            {
                "label": "Hipotenusa",
                "fn": hypotenuse,
                "fn_name": "hypotenuse",
                "params": ["leg_a", "leg_b"],
            },
            {
                "label": "Cateto desconocido",
                "fn": leg,
                "fn_name": "leg",
                "params": ["hypotenuse", "known_leg"],
            },
            {
                "label": "Área",
                "fn": rt_area,
                "fn_name": "rt_area",
                "params": ["leg_a", "leg_b"],
            },
            {
                "label": "Perímetro",
                "fn": rt_perimeter,
                "fn_name": "rt_perimeter",
                "params": ["leg_a", "leg_b"],
            },
            {
                "label": "Ángulo desde catetos",
                "fn": angle_from_legs,
                "fn_name": "angle_from_legs",
                "params": ["opposite_leg", "adjacent_leg"],
            },
            {
                "label": "Cateto desde hipotenusa + ángulo",
                "fn": leg_from_hypotenuse_angle,
                "fn_name": "leg_from_hypotenuse_angle",
                "params": ["hypotenuse", "angle_degrees"],
            },
        ],
    },
    "3D": {
        "Esfera": [
            {
                "label": "Volumen",
                "fn": sphere_volume,
                "fn_name": "sphere_volume",
                "params": ["radius"],
            },
            {
                "label": "Área de superficie",
                "fn": sphere_surface,
                "fn_name": "sphere_surface",
                "params": ["radius"],
            },
            {
                "label": "Radio desde volumen",
                "fn": sphere_r_from_vol,
                "fn_name": "sphere_r_from_vol",
                "params": ["volume"],
            },
            {
                "label": "Radio desde área de superficie",
                "fn": sphere_r_from_surface,
                "fn_name": "sphere_r_from_surface",
                "params": ["surface_area"],
            },
            {
                "label": "Diámetro",
                "fn": sphere_diameter,
                "fn_name": "sphere_diameter",
                "params": ["radius"],
            },
            {
                "label": "Volumen de casquete esférico",
                "fn": spherical_cap_volume,
                "fn_name": "spherical_cap_volume",
                "params": ["radius", "cap_height"],
            },
        ],
        "Cubo": [
            {
                "label": "Volumen",
                "fn": cube_volume,
                "fn_name": "cube_volume",
                "params": ["side"],
            },
            {
                "label": "Área de superficie",
                "fn": cube_surface,
                "fn_name": "cube_surface",
                "params": ["side"],
            },
            {
                "label": "Diagonal de cara",
                "fn": face_diagonal,
                "fn_name": "face_diagonal",
                "params": ["side"],
            },
            {
                "label": "Diagonal espacial",
                "fn": space_diagonal,
                "fn_name": "space_diagonal",
                "params": ["side"],
            },
            {
                "label": "Lado desde volumen",
                "fn": cube_side_from_vol,
                "fn_name": "cube_side_from_vol",
                "params": ["volume"],
            },
            {
                "label": "Lado desde área de superficie",
                "fn": cube_side_from_surface,
                "fn_name": "cube_side_from_surface",
                "params": ["surface_area"],
            },
        ],
        "Cilindro": [
            {
                "label": "Volumen",
                "fn": cyl_volume,
                "fn_name": "cyl_volume",
                "params": ["radius", "height"],
            },
            {
                "label": "Área de superficie",
                "fn": cyl_surface,
                "fn_name": "cyl_surface",
                "params": ["radius", "height"],
            },
            {
                "label": "Área lateral",
                "fn": cyl_lateral,
                "fn_name": "cyl_lateral",
                "params": ["radius", "height"],
            },
            {
                "label": "Radio desde volumen",
                "fn": cyl_r_from_vol,
                "fn_name": "cyl_r_from_vol",
                "params": ["volume", "height"],
            },
            {
                "label": "Altura desde volumen",
                "fn": cyl_h_from_vol,
                "fn_name": "cyl_h_from_vol",
                "params": ["volume", "radius"],
            },
        ],
        "Cono": [
            {
                "label": "Volumen",
                "fn": cone_volume,
                "fn_name": "cone_volume",
                "params": ["radius", "height"],
            },
            {
                "label": "Área de superficie",
                "fn": cone_surface,
                "fn_name": "cone_surface",
                "params": ["radius", "height"],
            },
            {
                "label": "Área lateral",
                "fn": cone_lateral,
                "fn_name": "cone_lateral",
                "params": ["radius", "height"],
            },
            {
                "label": "Altura inclinada",
                "fn": slant_height,
                "fn_name": "slant_height",
                "params": ["radius", "height"],
            },
            {
                "label": "Radio desde volumen",
                "fn": cone_r_from_vol,
                "fn_name": "cone_r_from_vol",
                "params": ["volume", "height"],
            },
            {
                "label": "Altura desde volumen",
                "fn": cone_h_from_vol,
                "fn_name": "cone_h_from_vol",
                "params": ["volume", "radius"],
            },
        ],
    },
}

# Readable labels for each parameter, used in the interface.
PARAM_LABELS: Dict[str, str] = {
    "radius": "Radio",
    "area": "Área",
    "perimeter": "Perímetro",
    "angle_degrees": "Ángulo (grados)",
    "side": "Lado",
    "diagonal": "Diagonal",
    "base": "Base",
    "height": "Altura",
    "side_a": "Lado a",
    "side_b": "Lado b",
    "side_c": "Lado c",
    "hypotenuse": "Hipotenusa",
    "known_leg": "Cateto conocido",
    "leg_a": "Cateto a",
    "leg_b": "Cateto b",
    "opposite_leg": "Cateto opuesto",
    "adjacent_leg": "Cateto adyacente",
    "surface_area": "Área de superficie",
    "cap_height": "Altura del casquete",
    "volume": "Volumen",
}