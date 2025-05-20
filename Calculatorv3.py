import tkinter as tk
from tkinter import ttk, messagebox
import math

# Material strength data (XY and Z in MPa)
materials = {
    "PLA Plus": (31.1, 16.7),
    "PLA Pro": (49.8, 36.5),
    "PLA CF": (31.2, 15.1),
    "PC": (69.1, 52.8),
    "PolyMax PLA": (41.3, 32.4),
    "Polymax PETG": (37.9, 29.4),
    "Polymax PC": (53.4, 41.4),
    "Polymax PC-FR": (67, 46),
    "CoPa": (78, 45.8),
    "PPS-CF": (142, 36),
    "PA6-CF20": (109.3, 54),
    "PA6-GF25": (80.1, 60.7),
    "PET-CF17": (65.9, 27.9),
    "PA12-CF10": (77.4, 52.2),
    "PA612-CF15": (52.2, 48.3),
    "PC-ABS": (39.9, 22.9),
    "PC-PBT": (50.4, 37.9),
    "Petg-CF": (59.8, 41.1),
    "PAHT-CF": (92, 47),
    "ABS-GF": (68, 46),
    "ASA-CF": (34, 30)
}

def calculate_barlows():
    try:
        pressure = float(barlows_pressure_entry.get())  # MPa
        diameter = float(barlows_diameter_entry.get())  # mm
        selected_material = material_dropdown.get()

        xy_strength, z_strength = materials[selected_material]

        # Barlow’s formula: thickness = (P * D) / (2 * strength)
        t_xy = (pressure * diameter) / (2 * xy_strength)
        t_z = (pressure * diameter) / (2 * z_strength)

        # Apply factor and safety margin
        t_xy = round(t_xy * 0.5386 + 0.5, 2)
        t_z = round(t_z * 0.5386 + 0.5, 2)

        barlows_result.config(text=f"Wall Thickness:\nXY: {t_xy} mm\nZ: {t_z} mm\n(0.5386 factor + 0.5 mm safety)")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def calculate_combined_gas_law():
    try:
        p1 = float(p1_entry.get())     # MPa
        v1 = float(v1_entry.get())     # cm³
        t1 = float(t1_entry.get())     # K
        v2 = float(v2_entry.get())     # cm³
        t2 = float(t2_entry.get())     # K

        p2 = (p1 * v1 * t2) / (v2 * t1)
        p2_result.config(text=f"Calculated P2: {round(p2, 2)} MPa")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def calculate_volume():
    try:
        d = float(diameter_entry.get())  # mm
        l = float(length_entry.get())    # mm
        v = math.pi * (d / 10 / 2) ** 2 * (l / 10)  # Convert mm to cm for cm³ result
        volume_result.config(text=f"Volume: {round(v, 2)} cm³")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for diameter and length.")

# GUI setup
root = tk.Tk()
root.title("3D Printed Pipe Calculator")

tabs = ttk.Notebook(root)
tab1 = tk.Frame(tabs)
tab2 = tk.Frame(tabs)
tab3 = tk.Frame(tabs)

tabs.add(tab1, text="Barlow's Thickness")
tabs.add(tab2, text="Combined Gas Law")
tabs.add(tab3, text="Cylinder Volume")
tabs.pack(expand=1, fill="both")

# Tab 1 – Barlow's
# Tab 1 – Barlow's
tk.Label(tab1, text="Pressure (P) in MPa:").pack()
barlows_pressure_entry = tk.Entry(tab1)
barlows_pressure_entry.pack()

tk.Label(tab1, text="Pipe Diameter (D) in mm:").pack()
barlows_diameter_entry = tk.Entry(tab1)
barlows_diameter_entry.pack()

tk.Label(tab1, text="Material:").pack()
material_dropdown = ttk.Combobox(tab1, values=list(materials.keys()))
material_dropdown.current(0)
material_dropdown.pack()

# Checkbox for custom input
use_custom = tk.IntVar()
tk.Checkbutton(tab1, text="Use custom XY/Z strength", variable=use_custom).pack()

tk.Label(tab1, text="Custom XY Strength (MPa):").pack()
custom_xy_entry = tk.Entry(tab1)
custom_xy_entry.pack()

tk.Label(tab1, text="Custom Z Strength (MPa):").pack()
custom_z_entry = tk.Entry(tab1)
custom_z_entry.pack()

def calculate_barlows():
    try:
        pressure = float(barlows_pressure_entry.get())
        diameter = float(barlows_diameter_entry.get())

        if use_custom.get():
            xy_strength = float(custom_xy_entry.get())
            z_strength = float(custom_z_entry.get())
        else:
            selected_material = material_dropdown.get()
            xy_strength, z_strength = materials[selected_material]

        t_xy = (pressure * diameter) / (2 * xy_strength)
        t_z = (pressure * diameter) / (2 * z_strength)

        # Apply factor and safety margin
        t_xy = round(t_xy * 0.5386 + 0.5, 2)
        t_z = round(t_z * 0.5386 + 0.5, 2)

        barlows_result.config(text=f"Wall Thickness:\nXY: {t_xy} mm\nZ: {t_z} mm\n(0.5386 factor + 0.5 mm safety)")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

tk.Button(tab1, text="Calculate Wall Thickness", command=calculate_barlows).pack()
barlows_result = tk.Label(tab1, text="")
barlows_result.pack()


# Tab 2 – Combined Gas Law
tk.Label(tab2, text="P1 (Chamber Pressure in MPa):").pack()
p1_entry = tk.Entry(tab2)
p1_entry.pack()

tk.Label(tab2, text="V1 (Barrel and Case Volume in cm³):").pack()
v1_entry = tk.Entry(tab2)
v1_entry.pack()

tk.Label(tab2, text="T1 (Chamber Temp in K, default 2000K):").pack()
t1_entry = tk.Entry(tab2)
t1_entry.insert(0, "2000")
t1_entry.pack()

tk.Label(tab2, text="V2 (Blast Chamber Volume in cm³):").pack()
v2_entry = tk.Entry(tab2)
v2_entry.pack()

tk.Label(tab2, text="T2 (Muzzle Temp in K):").pack()
t2_entry = tk.Entry(tab2)
t2_entry.pack()

tk.Button(tab2, text="Calculate P2", command=calculate_combined_gas_law).pack()
p2_result = tk.Label(tab2, text="")
p2_result.pack()

# Tab 3 – Volume Calculator
tk.Label(tab3, text="Diameter (mm):").pack()
diameter_entry = tk.Entry(tab3)
diameter_entry.pack()

tk.Label(tab3, text="Length (mm):").pack()
length_entry = tk.Entry(tab3)
length_entry.pack()

tk.Button(tab3, text="Calculate Volume (cm³)", command=calculate_volume).pack()
volume_result = tk.Label(tab3, text="")
volume_result.pack()

# Tab 4 – Muzzle Pressure Reference
tab4 = tk.Frame(tabs)
tabs.add(tab4, text="Muzzle Pressure Ref")

muzzle_label = tk.Label(tab4, text="Muzzle Pressures (Worst-Case / Best-Case Estimates)", font=("Arial", 10, "bold"))
muzzle_label.pack(pady=5)

# Text box with scroll
muzzle_text = tk.Text(tab4, wrap="word", height=25, width=70)
muzzle_text.pack()

# Muzzle pressure data
muzzle_data = """
Unit: Pressure in Atmospheres (atm)
Conversion: 1 atm = 0.101325 MPa

Assumption: Blast Chamber Dimensions — 1x1 inch (Pistol/Rifle), 2x2 inch (Shotguns)
Calculated using Combined Gas Law

--------------------------
WORST-CASE PRESSURE TABLE
--------------------------
Barrel Length   Caliber           Pressure (atm)
4 Inch          .22 LR            114.33
4 Inch          9mm +P            582.20
4 Inch          .45 ACP +P        623.87
4 Inch          .357 Magnum       793.56
10.5 Inch       5.56 NATO         1671.80
12.5 Inch       .308 Win.         3021.05
5 Inch          300 BLK Subsonic  622.80
7.5 Inch        300 BLK Super     1827.10
14.5 Inch       12 Gauge          726.03
14.5 Inch       20 Gauge          425.40
10.5 Inch       .410 Bore         137.84

--------------------------
BEST-CASE PRESSURE TABLE
--------------------------
Barrel Length   Caliber           Pressure (atm)
4 Inch          .22 LR            61.60
4 Inch          9mm +P            313.48
4 Inch          .45 ACP +P        335.77
4 Inch          .357 Magnum       427.32
10.5 Inch       5.56 NATO         899.77
12.5 Inch       .308 Win.         1627.40
5 Inch          300 BLK Subsonic  335.25
7.5 Inch        300 BLK Super     984.20
14.5 Inch       12 Gauge          391.04
14.5 Inch       20 Gauge          229.04
10.5 Inch       .410 Bore         74.24
"""

muzzle_text.insert("1.0", muzzle_data)
muzzle_text.config(state="disabled")

# Material Reference
def show_material_strengths():
    table = "Material Strength (MPa)\n\nMaterial\tXY\tZ\n"
    for name, (xy, z) in sorted(materials.items()):
        table += f"{name:15s}\t{xy:.1f}\t{z:.1f}\n"
    messagebox.showinfo("Material Strengths", table)

tk.Button(root, text="Show Material Strength Table", command=show_material_strengths).pack(pady=5)

root.mainloop()

