from letters import B

A = []
for l in B:
    a = []
    for x in l:
        a.append([round(x[0]/10+27, 2), round(x[1]/10+70, 2)])
    A.append(a)

print(A)
starting = """
M105
M109 S0
M82 ;absolute extrusion mode
G90
G1 X-20 Y220 Z15.0 F5000.0
G1 X13 Y220 F5000.0 ; Move to start position
M18 Z
M0
G92 X13 Y220 Z0.1
G1 Z10.0 F200
G92 E0
;LAYER_COUNT:1
;LAYER:0
M107"""
ending = """
G91 ;Relative positioning
G1 Z10 ;Raise Z more
M82 ;absolute extrusion mode
"""

# Набор строк G-code для движения по контурам буквы
gcode_lines = []
with open("test.gcode", 'w') as f:
    f.write(starting)

    for letter in A:
        f.write(f"Z1 F1000\n")
        f.write(f"G1 X{letter[0][0]} Y{letter[0][1]} F1000\n")
        f.write(f"G1 Z0 F100\n")

        for line in letter:
            f.write(f"G1 X{line[0]} Y{line[1]} F100\n")

        f.write("G1 Z1 F1000\n")
    f.write(ending)
    
    
