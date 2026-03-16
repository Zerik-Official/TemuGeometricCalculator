import customtkinter as ctk
from typing import Any, Callable, Dict, List

from services.shapes_2d import (
    circle_area, circle_perimeter, radius_from_area, radius_from_perimeter, circle_diameter, sector_area,
    square_area, square_perimeter, square_diagonal, side_from_area, side_from_perimeter, side_from_diagonal,
    rect_area, rect_perimeter, rect_diagonal, height_from_area, base_from_area, height_from_diagonal,
    tri_area, area_heron, tri_perimeter, tri_height_from_area, tri_base_from_area, semiperimeter,
    hypotenuse, leg, rt_area, rt_perimeter, angle_from_legs, leg_from_hypotenuse_angle,
)
from services.shapes_3d import (
    sphere_volume, sphere_surface, sphere_r_from_vol, sphere_r_from_surface, sphere_diameter, spherical_cap_volume,
    cube_volume, cube_surface, face_diagonal, space_diagonal, cube_side_from_vol, cube_side_from_surface,
    cyl_volume, cyl_surface, cyl_lateral, cyl_r_from_vol, cyl_h_from_vol,
    cone_volume, cone_surface, cone_lateral, slant_height, cone_r_from_vol, cone_h_from_vol,
)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# The best colors
ORANGE      = "#FB7701"
ORANGE_DARK = "#e06900"
WHITE       = "#FFFFFF"
TEXT_DARK   = "#1a1a1a"
TEXT_LIGHT  = "#FFFFFF"

FIGURES: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
    "2D": {
        "Círculo": [
            {"label": "Área",                  "fn": circle_area,          "params": ["radius"]},
            {"label": "Perímetro",             "fn": circle_perimeter,     "params": ["radius"]},
            {"label": "Radio desde área",      "fn": radius_from_area,     "params": ["area"]},
            {"label": "Radio desde perímetro", "fn": radius_from_perimeter,"params": ["perimeter"]},
            {"label": "Diámetro",              "fn": circle_diameter,      "params": ["radius"]},
            {"label": "Área de sector",        "fn": sector_area,          "params": ["radius", "angle_degrees"]},
        ],
        "Cuadrado": [
            {"label": "Área",                 "fn": square_area,          "params": ["side"]},
            {"label": "Perímetro",            "fn": square_perimeter,     "params": ["side"]},
            {"label": "Diagonal",             "fn": square_diagonal,      "params": ["side"]},
            {"label": "Lado desde área",      "fn": side_from_area,       "params": ["area"]},
            {"label": "Lado desde perímetro", "fn": side_from_perimeter,  "params": ["perimeter"]},
            {"label": "Lado desde diagonal",  "fn": side_from_diagonal,   "params": ["diagonal"]},
        ],
        "Rectángulo": [
            {"label": "Área",                   "fn": rect_area,            "params": ["base", "height"]},
            {"label": "Perímetro",              "fn": rect_perimeter,       "params": ["base", "height"]},
            {"label": "Diagonal",               "fn": rect_diagonal,        "params": ["base", "height"]},
            {"label": "Altura desde área",      "fn": height_from_area,     "params": ["area", "base"]},
            {"label": "Base desde área",        "fn": base_from_area,       "params": ["area", "height"]},
            {"label": "Altura desde diagonal",  "fn": height_from_diagonal, "params": ["diagonal", "base"]},
        ],
        "Triángulo": [
            {"label": "Área",                 "fn": tri_area,             "params": ["base", "height"]},
            {"label": "Área (Herón)",         "fn": area_heron,           "params": ["side_a", "side_b", "side_c"]},
            {"label": "Perímetro",            "fn": tri_perimeter,        "params": ["side_a", "side_b", "side_c"]},
            {"label": "Altura desde área",    "fn": tri_height_from_area, "params": ["area", "base"]},
            {"label": "Base desde área",      "fn": tri_base_from_area,   "params": ["area", "height"]},
            {"label": "Semiperímetro",        "fn": semiperimeter,        "params": ["side_a", "side_b", "side_c"]},
        ],
        "Triángulo Rectángulo": [
            {"label": "Hipotenusa",                             "fn": hypotenuse,               "params": ["leg_a", "leg_b"]},
            {"label": "Cateto desconocido",                     "fn": leg,                      "params": ["hypotenuse", "known_leg"]},
            {"label": "Área",                                    "fn": rt_area,                  "params": ["leg_a", "leg_b"]},
            {"label": "Perímetro",                               "fn": rt_perimeter,             "params": ["leg_a", "leg_b"]},
            {"label": "Ángulo desde catetos",                    "fn": angle_from_legs,          "params": ["opposite_leg", "adjacent_leg"]},
            {"label": "Cateto desde hipotenusa + ángulo",        "fn": leg_from_hypotenuse_angle,"params": ["hypotenuse", "angle_degrees"]},
        ],
    },
    "3D": {
        "Esfera": [
            {"label": "Volumen",                       "fn": sphere_volume,        "params": ["radius"]},
            {"label": "Área de superficie",            "fn": sphere_surface,       "params": ["radius"]},
            {"label": "Radio desde volumen",           "fn": sphere_r_from_vol,    "params": ["volume"]},
            {"label": "Radio desde área de superficie", "fn": sphere_r_from_surface,"params": ["surface_area"]},
            {"label": "Diámetro",                     "fn": sphere_diameter,      "params": ["radius"]},
            {"label": "Volumen de casquete esférico", "fn": spherical_cap_volume, "params": ["radius", "cap_height"]},
        ],
        "Cubo": [
            {"label": "Volumen",                      "fn": cube_volume,           "params": ["side"]},
            {"label": "Área de superficie",           "fn": cube_surface,          "params": ["side"]},
            {"label": "Diagonal de cara",             "fn": face_diagonal,         "params": ["side"]},
            {"label": "Diagonal espacial",            "fn": space_diagonal,        "params": ["side"]},
            {"label": "Lado desde volumen",           "fn": cube_side_from_vol,    "params": ["volume"]},
            {"label": "Lado desde área de superficie", "fn": cube_side_from_surface,"params": ["surface_area"]},
        ],
        "Cilindro": [
            {"label": "Volumen",         "fn": cyl_volume,   "params": ["radius", "height"]},
            {"label": "Área de superficie", "fn": cyl_surface,  "params": ["radius", "height"]},
            {"label": "Área lateral",      "fn": cyl_lateral,  "params": ["radius", "height"]},
            {"label": "Radio desde volumen","fn": cyl_r_from_vol,"params": ["volume", "height"]},
            {"label": "Altura desde volumen","fn": cyl_h_from_vol,"params": ["volume", "radius"]},
        ],
        "Cono": [
            {"label": "Volumen",         "fn": cone_volume,    "params": ["radius", "height"]},
            {"label": "Área de superficie","fn": cone_surface,   "params": ["radius", "height"]},
            {"label": "Área lateral",    "fn": cone_lateral,   "params": ["radius", "height"]},
            {"label": "Altura inclinada", "fn": slant_height,   "params": ["radius", "height"]},
            {"label": "Radio desde volumen","fn": cone_r_from_vol,"params": ["volume", "height"]},
            {"label": "Altura desde volumen","fn": cone_h_from_vol,"params": ["volume", "radius"]},
        ],
    },
}

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
}

def clear_frame(frame: ctk.CTkFrame) -> None:
    """Remueve todos los widgets hijos de un frame dado."""
    for widget in frame.winfo_children():
        widget.destroy()


def only_numbers(value: str) -> bool:
    """Validación para permitir solo números (y punto decimal) en los campos de entrada."""
    if value == "":
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False


def show_home(container: ctk.CTkFrame) -> None:
    """Muestra la vista principal para elegir dimensión 2D/3D."""
    clear_frame(container)

    ctk.CTkLabel(container, text="Selecciona una figura para continuar", font=("Arial", 16), text_color=TEXT_DARK).pack(pady=30)

    for dim in ("2D", "3D"):
        ctk.CTkButton(
            container,
            text=dim,
            width=120,
            fg_color=ORANGE,
            hover_color=ORANGE_DARK,
            text_color=TEXT_LIGHT,
            command=lambda d=dim: show_figures(container, d),
        ).pack(pady=8)


def show_figures(container: ctk.CTkFrame, dimension: str) -> None:
    """Muestra las figuras de la dimensión seleccionada."""
    clear_frame(container)

    ctk.CTkLabel(container, text=f"Selecciona una figura {dimension}", font=("Arial", 16), text_color=TEXT_DARK).pack(pady=20)

    for figure_name in FIGURES[dimension]:
        ctk.CTkButton(
            container,
            text=figure_name,
            width=180,
            fg_color=ORANGE,
            hover_color=ORANGE_DARK,
            text_color=TEXT_LIGHT,
            command=lambda name=figure_name: show_formulas(container, dimension, name),
        ).pack(pady=6)

    ctk.CTkButton(
        container,
        text="Atrás",
        width=120,
        fg_color=WHITE,
        hover_color="#f0f0f0",
        text_color=ORANGE,
        border_width=2,
        border_color=ORANGE,
        command=lambda: show_home(container),
    ).pack(pady=(20, 0))


def show_formulas(container: ctk.CTkFrame, dimension: str, figure_name: str) -> None:
    """Muestra las fórmulas disponibles de una figura seleccionada."""
    clear_frame(container)

    ctk.CTkLabel(container, text=figure_name, font=("Arial", 16), text_color=TEXT_DARK).pack(pady=20)

    for formula in FIGURES[dimension][figure_name]:
        ctk.CTkButton(
            container,
            text=formula["label"],
            width=200,
            fg_color=ORANGE,
            hover_color=ORANGE_DARK,
            text_color=TEXT_LIGHT,
            command=lambda f=formula: show_inputs(container, dimension, figure_name, f),
        ).pack(pady=5)

    ctk.CTkButton(
        container,
        text="Atrás",
        width=120,
        fg_color=WHITE,
        hover_color="#f0f0f0",
        text_color=ORANGE,
        border_width=2,
        border_color=ORANGE,
        command=lambda: show_figures(container, dimension),
    ).pack(pady=(20, 0))


def show_inputs(container: ctk.CTkFrame, dimension: str, figure_name: str, formula: Dict[str, Any]) -> None:
    """Muestra los campos de entrada para la fórmula elegida y calcula el resultado."""
    clear_frame(container)

    ctk.CTkLabel(
        container,
        text=f"{figure_name} — {formula['label']}",
        font=("Arial", 15),
        text_color=TEXT_DARK,
    ).pack(pady=20)

    vcmd = (container.register(only_numbers), "%P")
    entries: Dict[str, ctk.CTkEntry] = {}

    for param in formula["params"]:
        row = ctk.CTkFrame(container, fg_color="transparent")
        row.pack(pady=5)
        label_text = PARAM_LABELS.get(param, param)
        ctk.CTkLabel(row, text=label_text, width=140, anchor="e", text_color=TEXT_DARK).pack(side="left", padx=(0, 8))
        entry = ctk.CTkEntry(
            row,
            width=140,
            validate="key",
            validatecommand=vcmd,
            border_color=ORANGE,
            text_color=TEXT_DARK,
        )
        entry.pack(side="left")
        entries[param] = entry

    result_label = ctk.CTkLabel(container, text="", font=("Arial", 14), text_color=ORANGE)
    result_label.pack(pady=16)

    def calculate():
        try:
            args = [float(entries[p].get()) for p in formula["params"]]
            result = formula["fn"](*args)
            result_label.configure(text=f"Resultado: {result:.6f}".rstrip("0").rstrip("."), text_color=ORANGE)
        except ValueError:
            result_label.configure(text="Debes llenar todos los campos con números", text_color="red")
        except Exception as e:
            result_label.configure(text=f"Error: {e}", text_color="red")

    ctk.CTkButton(
        container,
        text="Calcular",
        fg_color=ORANGE,
        hover_color=ORANGE_DARK,
        text_color=TEXT_LIGHT,
        command=calculate,
    ).pack(pady=4)

    ctk.CTkButton(
        container,
        text="Probar otra formua",
        fg_color=WHITE,
        hover_color="#f0f0f0",
        text_color=ORANGE,
        border_width=2,
        border_color=ORANGE,
        command=lambda: show_formulas(container, dimension, figure_name),
    ).pack(pady=4)

    ctk.CTkButton(
        container,
        text="Volver a las figuras",
        fg_color=WHITE,
        hover_color="#f0f0f0",
        text_color=ORANGE,
        border_width=2,
        border_color=ORANGE,
        command=lambda: show_figures(container, dimension),
    ).pack(pady=4)


root = ctk.CTk()
root.title("ThemuCalculatorGeometric")
root.geometry("420x560")
root.resizable(False, False)
root.iconbitmap("temu.ico")
container = ctk.CTkFrame(root, fg_color=WHITE)
container.pack(fill="both", expand=True)

show_home(container)
root.mainloop()