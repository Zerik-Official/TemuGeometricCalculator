import os
import sys
from PIL import Image, ImageTk

from utils.commons import param_label_with_unit, to_display, to_metric, unit_suffix
from utils.geometry_data import FIGURES, PARAM_TYPE, RESULT_TYPE, unit_system

import customtkinter as ctk
from typing import Any, Dict

base = os.path.dirname(__file__)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Colors for the UI
ORANGE = "#FB7701"
ORANGE_DARK = "#e06900"
WHITE = "#FFFFFF"
TEXT_DARK = "#1a1a1a"
TEXT_LIGHT = "#FFFFFF"

def clear_frame(frame: ctk.CTkFrame) -> None:
    """
    Removes all child widgets from a given frame.
    
    Args:
        frame (ctk.CTkFrame): The frame to clear.
    Returns:
        None
    """

    for widget in frame.winfo_children():
        widget.destroy()


def only_numbers(value: str) -> bool:
    """
    Validates that only numbers are allowed in the input fields.

    Args:
        value (str): The current value of the input field.
    Returns:
        bool: True if the value is empty or can be converted to a float, False otherwise
    """
    if value == "":
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False

def show_home(container: ctk.CTkFrame) -> None:
    """
    Displays the main view.
    Includes unit system selector (Metric / Imperial)
    and the buttons to choose 2D or 3D dimension.

    Args:
        container (ctk.CTkFrame): The frame where the home view will be displayed.
    Returns:
        None
    """
    global unit_system

    clear_frame(container)

    if not sys.platform.startswith("win"):
        try:
            logo_img = Image.open(os.path.join(base, "temu.png"))
            logo_img = logo_img.resize((80, 80), Image.LANCZOS)
            logo_ctk = ctk.CTkImage(light_image=logo_img, size=(80, 80))
            ctk.CTkLabel(container, image=logo_ctk, text="").pack(pady=(30, 8))
        except Exception:
            pass
        ctk.CTkLabel(container, text="Selecciona una figura para continuar", font=("Arial", 16), text_color=TEXT_DARK).pack(pady=(0, 16))
    else:
        ctk.CTkLabel(container, text="Selecciona una figura para continuar", font=("Arial", 16), text_color=TEXT_DARK).pack(pady=(30, 16))

    ctk.CTkLabel(container, text="Sistema de unidades", font=("Arial", 13), text_color=TEXT_DARK,).pack()

    unit_var = ctk.StringVar(value=unit_system)

    unit_row = ctk.CTkFrame(container, fg_color="transparent")
    unit_row.pack(pady=(4, 20))

    def on_unit_change(selected: str) -> None:
        global unit_system
        unit_system = selected

    ctk.CTkRadioButton(unit_row, text="Métrico (m)", variable=unit_var, value="metric", fg_color=ORANGE, hover_color=ORANGE_DARK, text_color=TEXT_DARK, command=lambda: on_unit_change("metric")).pack(side="left", padx=16)

    ctk.CTkRadioButton(unit_row, text="Imperial (ft)", variable=unit_var, value="imperial", fg_color=ORANGE, hover_color=ORANGE_DARK, text_color=TEXT_DARK, command=lambda: on_unit_change("imperial")).pack(side="left", padx=16)

    for dim in ("2D", "3D"):
        ctk.CTkButton( container, text=dim, width=120, fg_color=ORANGE, hover_color=ORANGE_DARK, text_color=TEXT_LIGHT, command=lambda d=dim: show_figures(container, d)).pack(pady=8)


def show_figures(container: ctk.CTkFrame, dimension: str) -> None:
    """
    Displays the figures of the selected dimension.
    
    Args:
        container (ctk.CTkFrame): The frame where the figures will be displayed.
        dimension (str): "2D" or "3D", depending on the user's choice.
    Returns:
        None
    """
    clear_frame(container)

    ctk.CTkLabel(container, text=f"Selecciona una figura {dimension}", font=("Arial", 16), text_color=TEXT_DARK,).pack(pady=20)

    for figure_name in FIGURES[dimension]:
        ctk.CTkButton( container, text=figure_name, width=180, fg_color=ORANGE, hover_color=ORANGE_DARK, text_color=TEXT_LIGHT, command=lambda name=figure_name: show_formulas(container, dimension, name)).pack(pady=6)

    ctk.CTkButton(container, text="Atrás", width=120, fg_color=WHITE, hover_color="#f0f0f0", text_color=ORANGE, border_width=2, border_color=ORANGE, command=lambda: show_home(container)).pack(pady=(20, 0))


def show_formulas(container: ctk.CTkFrame, dimension: str, figure_name: str) -> None:
    """
    Displays the available formulas for the selected figure.
    
    Args:
        container (ctk.CTkFrame): The frame where the formulas will be displayed.
        dimension (str): "2D" or "3D", depending on the user's choice.
        figure_name (str): The name of the selected figure.
    Returns:
        None
    """
    clear_frame(container)

    ctk.CTkLabel(container, text=figure_name, font=("Arial", 16), text_color=TEXT_DARK).pack(pady=20)

    for formula in FIGURES[dimension][figure_name]:
        ctk.CTkButton(container, text=formula["label"], width=200, fg_color=ORANGE, hover_color=ORANGE_DARK, text_color=TEXT_LIGHT, command=lambda f=formula: show_inputs(container, dimension, figure_name, f)).pack(pady=5)

    ctk.CTkButton(container, text="Atrás", width=120, fg_color=WHITE, hover_color="#f0f0f0", text_color=ORANGE, border_width=2, border_color=ORANGE, command=lambda: show_figures(container, dimension),
    ).pack(pady=(20, 0))


def show_inputs(container: ctk.CTkFrame,dimension: str,figure_name: str,formula: Dict[str, Any]) -> None:
    """
    Shows the input fields for the selected formula and calculates the result.

    When the unit system is imperial:
    - The field labels display the unit in feet (e.g., "Radius (ft)").
    - The entered values are converted to metric before calculation.
    - The result is converted from metric to feet before being displayed, 
        along with its correct unit (ft, ft², ft³ or °).

    Args:
        container (ctk.CTkFrame): The frame where the input fields will be displayed
        dimension (str): "2D" or "3D", depending on the user's choice.
        figure_name (str): The name of the selected figure.
        formula (Dict[str, Any]): A dictionary containing the formula function, its label and parameters.
    Returns:
        None
    """
    clear_frame(container)

    ctk.CTkLabel(container, text=f"{figure_name} — {formula['label']}", font=("Arial", 15), text_color=TEXT_DARK).pack(pady=20)

    vcmd = (container.register(only_numbers), "%P")
    entries: Dict[str, ctk.CTkEntry] = {}

    for param in formula["params"]:
        row = ctk.CTkFrame(container, fg_color="transparent")
        row.pack(pady=5)
        label_text = param_label_with_unit(param)
        ctk.CTkLabel(row, text=label_text, width=160, anchor="e", text_color=TEXT_DARK).pack(side="left", padx=(0, 8))
        entry = ctk.CTkEntry(row, width=120, validate="key", validatecommand=vcmd, border_color=ORANGE, text_color=TEXT_DARK)
        entry.pack(side="left")
        entries[param] = entry

    result_label = ctk.CTkLabel(
        container, text="", font=("Arial", 14), text_color=ORANGE
    )
    result_label.pack(pady=16)

    def calculate() -> None:
        """
        Calculates the result of the formula based on the entered values,
        applying unit conversions if necessary, and displays it.

        Args:
            None
        Returns:
            None
        """
        
        try:
            args = []
            for p in formula["params"]:
                raw = float(entries[p].get())
                measure_type = PARAM_TYPE.get(p, "length")
                args.append(to_metric(raw, measure_type))

            result_metric = formula["fn"](*args)

            fn_name = formula["fn_name"]
            result_type = RESULT_TYPE.get(fn_name, "length")
            result_display = to_display(result_metric, result_type)
            suffix = unit_suffix(result_type)

            formatted = f"{result_display:.6f}".rstrip("0").rstrip(".")
            result_label.configure(text=f"Resultado: {formatted} {suffix}".strip(), text_color=ORANGE)
        except ValueError as e:
            msg = str(e)
            if not msg:
                msg = "Debes llenar todos los campos con números"
            result_label.configure(text=msg, text_color="red")
        except Exception as e:
            result_label.configure(text=f"Error: {e}", text_color="red")

    ctk.CTkButton(container, text="Calcular", fg_color=ORANGE, hover_color=ORANGE_DARK, text_color=TEXT_LIGHT, command=calculate).pack(pady=4)

    ctk.CTkButton(container, text="Probar otra fórmula", fg_color=WHITE, hover_color="#f0f0f0", text_color=ORANGE, border_width=2, border_color=ORANGE, command=lambda: show_formulas(container, dimension, figure_name)).pack(pady=4)

    ctk.CTkButton(container, text="Volver a las figuras", fg_color=WHITE, hover_color="#f0f0f0", text_color=ORANGE, border_width=2, border_color=ORANGE, command=lambda: show_figures(container, dimension)).pack(pady=4)

root = ctk.CTk()
root.title("ThemuCalculatorGeometric")
root.geometry("420x580")
root.resizable(False, False)

if sys.platform.startswith("win"):
    root.iconbitmap(os.path.join(base, "temu.ico"))
else:
    try:
        img = Image.open(os.path.join(base, "temu.png"))
        icon = ImageTk.PhotoImage(img)
        root.iconphoto(True, icon)
    except Exception:
        pass

container = ctk.CTkFrame(root, fg_color=WHITE)
container.pack(fill="both", expand=True)

show_home(container)
root.mainloop()