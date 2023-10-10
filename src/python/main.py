import numpy as np

import input_page
from Elemento import *

elementos, nos = input_page.run()

gls_alpha = []
gls_beta = []

desl_alpha = []
desl_beta = []

for _, no in nos.items():
    for gl in no.gl:
        if isinstance(gl, Gl):
            if gl.known:
                try:
                    gls_beta.index(gl)
                except ValueError:
                    gls_beta.append(gl)
                    try:
                        desl_beta.append(float(gl.dt_value))
                    except TypeError:
                        desl_beta.append(0)
            else:
                try:
                    gls_alpha.index(gl)
                except ValueError:
                    gls_alpha.append(gl)
                    desl_alpha.append(0)


gls = []
gls.extend(gls_alpha)
gls.extend(gls_beta)

desl = []
desl.extend(desl_alpha)
desl.extend(desl_beta)

desl_alpha = np.array(desl_alpha)
desl_beta = np.array(desl_beta)

desl = np.array(desl)

forces = []
for gl in gls:
    try:
        float(gl.force)
        forces.append(float(gl.force))
    except TypeError:
        forces.append(0)

forces = np.array(forces)

mat_localizacao = []
for el in elementos:
    temp = [gls.index(el.no1.gl[0]), gls.index(el.no1.gl[1])]
    if el.el_type == "Viga" or el.el_type == "Portico":
        temp.append(gls.index(el.no1.gl[2]))
    temp.append(gls.index(el.no2.gl[0]))
    temp.append(gls.index(el.no2.gl[1]))
    if el.el_type == "Viga" or el.el_type == "Portico":
        temp.append(gls.index(el.no2.gl[2]))
    mat_localizacao.append(temp.copy())
    temp.clear()

matriz_rigidez_global = np.zeros((len(gls), len(gls)))
for el in elementos:
    if el.el_type == "Mola" or el.el_type == "Barra":
        for x, l in enumerate([gls.index(el.no1.gl[0]), gls.index(el.no1.gl[1]), gls.index(el.no2.gl[0]), gls.index(el.no2.gl[1])]):
            for y, c in enumerate([gls.index(el.no1.gl[0]), gls.index(el.no1.gl[1]), gls.index(el.no2.gl[0]), gls.index(el.no2.gl[1])]):
                matriz_rigidez_global[l, c] += el.matriz_local()[x, y]
    elif el.el_type == "Viga" or el.el_type == "Portico":
        for x, l in enumerate([gls.index(el.no1.gl[0]), gls.index(el.no1.gl[1]), gls.index(el.no1.gl[2]), gls.index(el.no2.gl[0]), gls.index(el.no2.gl[1]), gls.index(el.no2.gl[2])]):
            for y, c in enumerate([gls.index(el.no1.gl[0]), gls.index(el.no1.gl[1]), gls.index(el.no1.gl[2]), gls.index(el.no2.gl[0]), gls.index(el.no2.gl[1]), gls.index(el.no2.gl[2])]):
                matriz_rigidez_global[l, c] += el.matriz_local()[x, y]

desl_alpha = np.linalg.lstsq(matriz_rigidez_global[:len(gls_alpha), :len(gls_alpha)], (forces[:len(gls_alpha)] - np.dot(matriz_rigidez_global[:len(gls_alpha), len(gls_alpha):len(gls_beta) + len(gls_alpha)], desl_beta)), rcond=None)[0]

pass
