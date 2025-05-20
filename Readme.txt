=======================================
 3D Printed "Pipe" Calculator v1.0
=======================================

This tool helps makers calculate safe wall thickness for 3D printed "pipes" using:
- **Barlow's Formula**
- **Combined Gas Law**

✅ Works for both **XY** and **Z-axis** tensile strength
✅ Includes a material selector for common filaments
✅ Adds a built-in **0.5 mm safety margin**
✅ Final thickness is scaled by **0.5386** as a design efficiency factor

---------------------------------------
 HOW TO USE
---------------------------------------

1. 📌 **Select Your Material**
   - Choose your filament from the dropdown. XY and Z strength values are used internally.

2. 🧮 **Barlow’s Formula Calculator**
   - Input:
     - Internal Pressure (P) in MPa
     - Outer Diameter (D) in mm
   - Output:
     - Required Wall Thickness (in mm, includes 0.5 mm safety margin)

3. 🧪 **Combined Gas Law Calculator**
   - Input:
     - P1: (Chamber Pressure) in MPa
     - V1: (Barrel + Case Volume) in cm³
     - T1: (Chamber Temperature) in Kelvin (default is 2000K)
     - V2: (Blast Chamber Volume) in cm³
     - T2: (Muzzle Temperature) in Kelvin

   - Output:
     - Estimated Final Pressure (P2) in MPa
     - Value automatically used in Barlow’s Formula, if desired

📎 Volume calculators are available for V1 and V2 using the cylinder volume formula:
    Volume = π × (radius)² × height

🧪 T2 is estimated based on typical nozzle/air values (adjustable in future versions).

---------------------------------------
 MATERIAL STRENGTHS REFERENCE
---------------------------------------

Here’s a simplified version of the strength chart used:

(Material – XY MPa / Z MPa)

- PLA Plus ............ 31 / 17
- PLA Pro .............. 50 / 36
- PLA CF ............... 31 / 15
- PC ..................... 69 / 53
- PolyMax PLA .... 41 / 32
- PolyMax PETG ... 38 / 29
- PolyMax PC ........ 53 / 41
- CoPa .................. 78 / 46
- PPS-CF .............. 142 / 36
- PA6-CF20 .......... 109 / 54
- PA6-GF25 .......... 80 / 61
- PA12-CF10 ........ 77 / 52
- PC-ABS .............. 40 / 23
- Petg-CF .............. 60 / 41
- PAHT-CF ............ 92 / 47
- ASA-CF .............. 34 / 30
*Sourced From PolyMaker & BambuLab

*Lean toward Z strength when unsure — it’s often the weakest axis in printing.
*I would personally stay close to the MWT(minimum wall thickness) for all the
Baffle structures in your "pipe" 

---------------------------------------
 MADE BY Natenate77/Nsup3032 Odysee
---------------------------------------

Created with Python + Tkinter  
Questions? Suggestions? Contact me via X: Natenate77