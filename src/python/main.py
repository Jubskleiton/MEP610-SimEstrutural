import numpy as np
import input_page
from Elemento import *

elementos, nos = input_page.run()

gls_n_k = []
gls_k = []

for _, no in nos.items():
    for gl in no.gl:
        if isinstance(gl, Gl):
            if gl.known:
                try:
                    gls_k.index(gl)
                except ValueError:
                    gls_k.append(gl)
            else:
                try:
                    gls_n_k.index(gl)
                except ValueError:
                    gls_n_k.append(gl)


gls = []
gls.extend(gls_n_k)
gls.extend(gls_k)

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
print(mat_localizacao)

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

print(matriz_rigidez_global)
pass
