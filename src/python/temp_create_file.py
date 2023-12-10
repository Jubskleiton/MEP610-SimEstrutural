import math
from Elemento import *

def abc():
    #    x1 y1 x2 y2  u1    v1    u2    v2      u1 v1 u2 v2 fu1    fv1    fu2    fv2    fu1 fv1 fu2 fv2 fixu1 fixv1 fixu2 fixv2   k
    info = [
        [-1, 1, 0, 3, False, False, False, False, 0, 0, 0, 0, True, False, False, True, 7,  0,  0,  -5,  False, False, False, False, 2],
        [-1, 1, 0, 2, False, False, False, False, 0, 0, 0, 0, True, False, False, False, 7,  0,  0,  0,  False, False, False, False, 2],
        [0, 0, -1, 1, True, True, False, False, 0, 0, 0, 0, False, False, True, False, 0,  0,  7,  0,  True, True, False, False, 2],
        [0, 2, 0, 3, False, False, False, False, 0, 0, 0, 0, False, False, False, True, 0,  0,  0,  -5,  False, False, False, False, 2],
        [0, 0, 0, 2, True, True, False, False, 0, 0, 0, 0, False, False, False, False, 0,  0,  0,  0,  True, True, False, False, 1],
        [0, 0, 1, 1, True, True, False, False, 0, 0, 0, 0, False, False, False, True, 0,  0,  0,  3,  True, True, False, False, 5],
        [0, 3, 2, 3, False, False, False, False, 0, 0, 0, 0, False, True, False, True, 0,  -5,  0,  -10,  False, False, False, False, 5],
        [0, 2, 2, 3, False, False, False, False, 0, 0, 0, 0, False, False, False, True, 0,  0,  0,  -10,  False, False, False, False, 5],
        [0, 2, 3, 2, False, False, True, True, 0, 0, 0, -5, False, False, False, False, 0,  0,  0,  0,  False, False, True, False, 5],
        [0, 2, 2, 1, False, False, False, False, 0, 0, 0, 0, False, False, False, False, 0,  0,  0,  0,  False, False, False, False, 5],
        [0, 2, 1, 1, False, False, False, False, 0, 0, 0, 0, False, False, False, True, 0,  0,  0,  3,  False, False, False, False, 4],
        [2, 3, 3, 2, False, False, True, True, 0, 0, 0, -5, False, True, False, False, 0, -10,  0,  0,  False, False, True, False, 4],
        [1, 1, 2, 1, False, False, False, False, 0, 0, 0, 0, False, True, False, False, 0, 3,  0,  0,  False, False, False, False, 4],
        [2, 1, 3, 2, False, False, True, True, 0, 0, 0, -5, False, False, False, False, 0, 0,  0,  0,  False, False, True, False, 4]
        ]

    elementos = []
    nos = {}

    for x1, y1, x2, y2, u1, v1, u2, v2, inp_u1, inp_v1, inp_u2, inp_v2, fu1, fv1, fu2, fv2, inp_fu1, inp_fv1, inp_fu2, inp_fv2, fix_u1, fix_v1, fix_u2, fix_v2, k in info:
        if (float(x2) - float(x1)) != 0:
            if math.atan2(float(y2) - float(y1), float(x2) - float(x1)) > 0:
                theta = math.atan2((float(y2) - float(y1)), (float(x2) - float(x1)))
            else:
                theta = 2 * math.pi + math.atan2((float(y2) - float(y1)), (float(x2) - float(x1)))
        else:
            theta = math.pi / 2

        gl1 = Gl(x1, u1, "x", dt_value=float(inp_u1) if u1 else None, force=float(inp_fu1) if fu1 else None, force_known=fu1, fix=fix_u1)
        gl2 = Gl(y1, v1, "y", dt_value=float(inp_v1) if v1 else None, force=float(inp_fv1) if fv1 else None, force_known=fv1, fix=fix_v1)
        gl3 = Gl(x2, u2, "x", dt_value=float(inp_u2) if u2 else None, force=float(inp_fu2) if fu2 else None, force_known=fu2, fix=fix_u2)
        gl4 = Gl(y2, v2, "y", dt_value=float(inp_v2) if v2 else None, force=float(inp_fv2) if fv2 else None, force_known=fv2, fix=fix_v2)
        # verifica se o grau ja existe (broken)
        # graus_de_liberdade[x1()] = gl1
        # graus_de_liberdade[y1()] = gl2
        # graus_de_liberdade[x2()] = gl3
        # graus_de_liberdade[y2()] = gl4

        no1 = No(gl1, gl2) if not isinstance(nos.get(str(x1) + "," + str(y1)), No) else nos.get(str(x1) + "," + str(y1))
        no2 = No(gl3, gl4) if not isinstance(nos.get(str(x2) + "," + str(y2)), No) else nos.get(str(x2) + "," + str(y2))

        nos[str(x1) + "," + str(y1)] = no1
        nos[str(x2) + "," + str(y2)] = no2

        elementos.append(Elemento(no1, no2, theta, "Mola", k=k))

    return elementos, nos
