import flet as ft
from Elemento import *

elementos = []
nos = {}


def inp_page(page: ft.Page):
    page.window_min_height = 780
    page.window_min_width = 950
    page.window_max_height = 780
    page.window_max_width = 950

    def button_click(e):
        match dropdown.value:
            case "Mola":
                if x1() and y1() and x2() and y2() and k() and (not checkbox_u1() or input_u1()) and (not checkbox_v1() or input_v1()) and (not checkbox_u2() or input_u2()) and (not checkbox_v2() or input_v2()):
                    if (float(x2()) - float(x1())) != 0:
                        if math.atan2(float(y2()) - float(y1()), float(x2()) - float(x1())) > 0:
                            theta = math.atan2((float(y2()) - float(y1())), (float(x2()) - float(x1())))
                        else:
                            theta = 2*math.pi + math.atan2((float(y2()) - float(y1())), (float(x2()) - float(x1())))
                    else:
                        theta = math.pi/2

                    gl1 = Gl(x1(), checkbox_u1(), "x", dt_value=float(input_u1()) if checkbox_u1() else None, force=float(input_fu1()) if checkbox_fu1() else None, force_known=checkbox_fu1, fix=apoio_u1)
                    gl2 = Gl(y1(), checkbox_v1(), "y", dt_value=float(input_v1()) if checkbox_v1() else None, force=float(input_fv1()) if checkbox_fv1() else None, force_known=checkbox_fv1, fix=apoio_v1)
                    gl3 = Gl(x2(), checkbox_u2(), "x", dt_value=float(input_u2()) if checkbox_u2() else None, force=float(input_fu2()) if checkbox_fu2() else None, force_known=checkbox_fu2, fix=apoio_u2)
                    gl4 = Gl(y2(), checkbox_v2(), "y", dt_value=float(input_v2()) if checkbox_v2() else None, force=float(input_fv2()) if checkbox_fv2() else None, force_known=checkbox_fv2, fix=apoio_v2)
                    # verifica se o grau ja existe (broken)
                    # graus_de_liberdade[x1()] = gl1
                    # graus_de_liberdade[y1()] = gl2
                    # graus_de_liberdade[x2()] = gl3
                    # graus_de_liberdade[y2()] = gl4

                    no1 = No(gl1, gl2) if not isinstance(nos.get(x1()+","+y1()), No) else nos.get(x1()+","+y1())
                    no2 = No(gl3, gl4) if not isinstance(nos.get(x2()+","+y2()), No) else nos.get(x2()+","+y2())

                    nos[x1()+","+y1()] = no1
                    nos[x2()+","+y2()] = no2

                    elementos.append(Elemento(no1, no2, theta, "Mola", k=k()))
                else:
                    print("falta")
            case "Viga":
                if x1() and y1() and x2() and y2() and (not checkbox_u1() or input_u1()) and (not checkbox_v1() or input_v1()) and (not checkbox_θ1() or input_θ1()) and (not checkbox_u2() or input_u2()) and (not checkbox_v2() or input_v2()) and (not checkbox_θ2() or input_θ2()) and l() and ei():
                    if (float(x2()) - float(x1())) != 0:
                        if math.atan2(float(y2()) - float(y1()), float(x2()) - float(x1())) > 0:
                            theta = math.atan2((float(y2()) - float(y1())), (float(x2()) - float(x1())))
                        else:
                            theta = 2 * math.pi + math.atan2((float(y2()) - float(y1())), (float(x2()) - float(x1())))
                    else:
                        theta = math.pi / 2
                    gl1 = Gl(x1(), checkbox_u1(), "x", dt_value=float(input_u1()) if checkbox_u1() else 0, force=float(input_fu1()) if checkbox_fu1() else None, force_known=checkbox_fu1, fix=apoio_u1)
                    gl2 = Gl(y1(), checkbox_v1(), "y", dt_value=float(input_v1()) if checkbox_v1() else 0, force=float(input_fv1()) if checkbox_fv1() else None, force_known=checkbox_fv1, fix=apoio_v1)
                    gl3 = Gl(x2(), checkbox_u2(), "x", dt_value=float(input_u2()) if checkbox_u2() else 0, force=float(input_fu2()) if checkbox_fu2() else None, force_known=checkbox_fu2, fix=apoio_u2)
                    gl4 = Gl(y2(), checkbox_v2(), "y", dt_value=float(input_v2()) if checkbox_v2() else 0, force=float(input_fv2()) if checkbox_fv2() else None, force_known=checkbox_fv2, fix=apoio_v2)
                    gl5 = Gl(0, checkbox_θ1(), "θ", dt_value=float(input_θ1()) if checkbox_θ1() else 0, force_known=input_tθ1, fix=apoio_θ1)
                    gl6 = Gl(0, checkbox_θ2(), "θ", dt_value=float(input_θ2()) if checkbox_θ2() else 0, force_known=input_tθ2, fix=apoio_θ2)

                    if isinstance(nos.get(x1() + "," + y1()), No):
                        if isinstance(nos.get(x1() + "," + y1()).gl[2], Gl):
                            no1 = nos.get(x1() + "," + y1())
                        else:
                            no1 = nos.get(x1() + "," + y1())
                            no1.gl3 = gl5
                    else:
                        no1 = No(gl1, gl2, gl3=gl5)

                    if isinstance(nos.get(x2() + "," + y2()), No):
                        if isinstance(nos.get(x2() + "," + y2()).gl[2], Gl):
                            no2 = nos.get(x2() + "," + y2())
                        else:
                            no2 = nos.get(x2() + "," + y2())
                            no2.gl3 = gl6
                    else:
                        no2 = No(gl3, gl4, gl3=gl6)

                    nos[x1() + "," + y1()] = no1
                    nos[x2() + "," + y2()] = no2

                    elementos.append(Elemento(no1, no2, theta, "Viga", l=l(), ei=ei()))
                else:
                    print("falta")
            case "Barra":
                if x1() and y1() and x2() and y2() and (not checkbox_u1() or input_u1()) and (not checkbox_v1() or input_v1()) and (not checkbox_u2() or input_u2()) and (not checkbox_v2() or input_v2()) and l() and ae():
                    if (float(x2()) - float(x1())) != 0:
                        if math.atan2(float(y2()) - float(y1()), float(x2()) - float(x1())) > 0:
                            theta = math.atan2((float(y2()) - float(y1())), (float(x2()) - float(x1())))
                        else:
                            theta = (2 * math.pi) + math.atan2((float(y2()) - float(y1())), (float(x2()) - float(x1())))
                    else:
                        theta = math.pi / 2

                    gl1 = Gl(x1(), checkbox_u1(), "x", dt_value=float(input_u1()) if checkbox_u1() else 0, force=float(input_fu1()) if checkbox_fu1() else None, force_known=checkbox_fu1, fix=apoio_u1)
                    gl2 = Gl(y1(), checkbox_v1(), "y", dt_value=float(input_v1()) if checkbox_v1() else 0, force=float(input_fv1()) if checkbox_fv1() else None, force_known=checkbox_fv1, fix=apoio_v1)
                    gl3 = Gl(x2(), checkbox_u2(), "x", dt_value=float(input_u2()) if checkbox_u2() else 0, force=float(input_fu2()) if checkbox_fu2() else None, force_known=checkbox_fu2, fix=apoio_u2)
                    gl4 = Gl(y2(), checkbox_v2(), "y", dt_value=float(input_v2()) if checkbox_v2() else 0, force=float(input_fv2()) if checkbox_fv2() else None, force_known=checkbox_fv2, fix=apoio_v2)

                    no1 = No(gl1, gl2) if not isinstance(nos.get(x1() + "," + y1()), No) else nos.get(x1() + "," + y1())
                    no2 = No(gl3, gl4) if not isinstance(nos.get(x2() + "," + y2()), No) else nos.get(x2() + "," + y2())

                    nos[x1() + "," + y1()] = no1
                    nos[x2() + "," + y2()] = no2

                    elementos.append(Elemento(no1, no2, theta, "Barra", l=l(), ae=ae()))
                else:
                    print("falta")
            case "Portico":  # missing θ GL
                if x1() and y1() and x2() and y2() and (not checkbox_u1() or input_u1()) and (not checkbox_v1() or input_v1()) and (not checkbox_θ1() or input_θ1()) and (not checkbox_u2() or input_u2()) and (not checkbox_v2() or input_v2()) and (not checkbox_θ2() or input_θ2()) and l() and ei():
                    if (float(x2()) - float(x1())) != 0:
                        if math.atan2(float(y2()) - float(y1()), float(x2()) - float(x1())) > 0:
                            theta = math.atan2((float(y2()) - float(y1())), (float(x2()) - float(x1())))
                        else:
                            theta = 2 * math.pi + math.atan2((float(y2()) - float(y1())), (float(x2()) - float(x1())))
                    else:
                        theta = math.pi / 2

                    gl1 = Gl(x1(), checkbox_u1(), "x", dt_value=float(input_u1()) if checkbox_u1() else 0, force=float(input_fu1()) if checkbox_fu1() else None, force_known=checkbox_fu1, fix=apoio_u1)
                    gl2 = Gl(y1(), checkbox_v1(), "y", dt_value=float(input_v1()) if checkbox_v1() else 0, force=float(input_fv1()) if checkbox_fv1() else None, force_known=checkbox_fv1, fix=apoio_v1)
                    gl3 = Gl(x2(), checkbox_u2(), "x", dt_value=float(input_u2()) if checkbox_u2() else 0, force=float(input_fu2()) if checkbox_fu2() else None, force_known=checkbox_fu2, fix=apoio_u2)
                    gl4 = Gl(y2(), checkbox_v2(), "y", dt_value=float(input_v2()) if checkbox_v2() else 0, force=float(input_fv2()) if checkbox_fv2() else None, force_known=checkbox_fv2, fix=apoio_v2)

                    no1 = No(gl1, gl2) if not isinstance(nos.get(x1() + "," + y1()), No) else nos.get(x1() + "," + y1())
                    no2 = No(gl3, gl4) if not isinstance(nos.get(x2() + "," + y2()), No) else nos.get(x2() + "," + y2())

                    nos[x1() + "," + y1()] = no1
                    nos[x2() + "," + y2()] = no2

                    elementos.append(Elemento(no1, no2, theta, "Portico", l=l(), ei=ei()))
                else:
                    print("falta")
        print(elementos, "\n", nos)

    def gl_check_box_change(e):
        if checkbox_u1():
            check_input.controls[0].controls[0].controls[1].visible = True   # input u1
        else:
            check_input.controls[0].controls[0].controls[1].visible = False
        if checkbox_v1():
            check_input.controls[0].controls[1].controls[1].visible = True   # input v1
        else:
            check_input.controls[0].controls[1].controls[1].visible = False
        if checkbox_θ1():
            check_input.controls[0].controls[2].controls[1].visible = True   # input θ1
        else:
            check_input.controls[0].controls[2].controls[1].visible = False
        if checkbox_u2():
            check_input.controls[0].controls[3].controls[1].visible = True   # input u2
        else:
            check_input.controls[0].controls[3].controls[1].visible = False
        if checkbox_v2():
            check_input.controls[0].controls[4].controls[1].visible = True   # input v2
        else:
            check_input.controls[0].controls[4].controls[1].visible = False
        if checkbox_θ2():
            check_input.controls[0].controls[5].controls[1].visible = True   # input θ2
        else:
            check_input.controls[0].controls[5].controls[1].visible = False
        page.update()

    def f_check_box_change(e):
        if checkbox_fu1():
            check_input.controls[1].controls[0].controls[1].visible = True   # input fu1
        else:
            check_input.controls[1].controls[0].controls[1].visible = False
        if checkbox_fv1():
            check_input.controls[1].controls[1].controls[1].visible = True   # input fv1
        else:
            check_input.controls[1].controls[1].controls[1].visible = False
        if checkbox_tθ1():
            check_input.controls[1].controls[2].controls[1].visible = True   # input tθ1
        else:
            check_input.controls[1].controls[2].controls[1].visible = False
        if checkbox_fu2():
            check_input.controls[1].controls[3].controls[1].visible = True   # input fu2
        else:
            check_input.controls[1].controls[3].controls[1].visible = False
        if checkbox_fv2():
            check_input.controls[1].controls[4].controls[1].visible = True   # input fv2
        else:
            check_input.controls[1].controls[4].controls[1].visible = False
        if checkbox_tθ2():
            check_input.controls[1].controls[5].controls[1].visible = True   # input tθ2
        else:
            check_input.controls[1].controls[5].controls[1].visible = False
        page.update()

    def dropdown_changed(e):
        match dropdown.value:
            case "Mola":
                input_field.controls[0].controls[4].visible = False  # Apoio θ1
                input_field.controls[1].controls[4].visible = False  # Apoio θ2

                input_field.controls[2].controls[0].visible = True   # K
                input_field.controls[2].controls[1].visible = False  # L
                input_field.controls[2].controls[2].visible = False  # EI
                input_field.controls[2].controls[3].visible = False  # AE

                check_input.controls[0].controls[2].controls[0].visible = False  # checkbox θ1
                check_input.controls[0].controls[2].controls[1].visible = False  # input θ1
                check_input.controls[0].controls[5].controls[0].visible = False  # checkbox θ2
                check_input.controls[0].controls[5].controls[1].visible = False  # input θ2

                check_input.controls[1].controls[2].controls[0].visible = False  # checkbox tθ1
                check_input.controls[1].controls[2].controls[1].visible = False  # input tθ1
                check_input.controls[1].controls[5].controls[0].visible = False  # checkbox tθ2
                check_input.controls[1].controls[5].controls[1].visible = False  # input tθ2
            case  "Viga":
                input_field.controls[0].controls[4].visible = True   # Apoio θ1
                input_field.controls[1].controls[4].visible = True   # Apoio θ2

                input_field.controls[2].controls[0].visible = False  # K
                input_field.controls[2].controls[1].visible = True   # L
                input_field.controls[2].controls[2].visible = True   # EI
                input_field.controls[2].controls[3].visible = False  # AE

                check_input.controls[0].controls[2].controls[0].visible = True   # checkbox θ1
                check_input.controls[0].controls[5].controls[0].visible = True   # checkbox θ2

                check_input.controls[1].controls[2].controls[0].visible = True  # checkbox tθ1
                check_input.controls[1].controls[5].controls[0].visible = True  # checkbox tθ2
            case "Barra":
                input_field.controls[0].controls[4].visible = False  # Apoio θ1
                input_field.controls[1].controls[4].visible = False  # Apoio θ2

                input_field.controls[2].controls[0].visible = False  # K
                input_field.controls[2].controls[1].visible = True   # L
                input_field.controls[2].controls[2].visible = False  # EI
                input_field.controls[2].controls[3].visible = True   # AE

                check_input.controls[0].controls[2].controls[0].visible = False  # checkbox θ1
                check_input.controls[0].controls[2].controls[1].visible = False  # input θ1
                check_input.controls[0].controls[5].controls[0].visible = False  # checkbox θ2
                check_input.controls[0].controls[5].controls[1].visible = False  # input θ2

                check_input.controls[1].controls[2].controls[0].visible = False  # checkbox tθ1
                check_input.controls[1].controls[2].controls[1].visible = False  # input tθ1
                check_input.controls[1].controls[5].controls[0].visible = False  # checkbox tθ2
                check_input.controls[1].controls[5].controls[1].visible = False  # input tθ2
            case "Portico":
                input_field.controls[0].controls[4].visible = True   # Apoio θ1
                input_field.controls[1].controls[4].visible = True   # Apoio θ2

                input_field.controls[2].controls[0].visible = False  # K
                input_field.controls[2].controls[1].visible = True   # L
                input_field.controls[2].controls[2].visible = True   # EI
                input_field.controls[2].controls[3].visible = False  # AE

                check_input.controls[0].controls[2].controls[0].visible = True   # checkbox θ1
                check_input.controls[0].controls[2].controls[1].visible = False  # input θ1
                check_input.controls[0].controls[5].controls[0].visible = True   # checkbox θ2
                check_input.controls[0].controls[5].controls[1].visible = False  # input θ2

                check_input.controls[1].controls[2].controls[0].visible = True  # checkbox tθ1
                check_input.controls[1].controls[2].controls[1].visible = False  # input tθ1
                check_input.controls[1].controls[5].controls[0].visible = True  # checkbox tθ2
                check_input.controls[1].controls[5].controls[1].visible = False  # input tθ2
            case _:
                print("????????????????")
        input_field.update()
        check_input.update()

    # main page
    # select dropdown
    dropdown = ft.Dropdown(width=200,
                           options=[ft.dropdown.Option("Mola"),
                                    ft.dropdown.Option("Viga"),
                                    ft.dropdown.Option("Barra"),
                                    ft.dropdown.Option("Portico")],
                           value="Mola",
                           on_change=dropdown_changed)
    # pos input
    input_field = ft.Column([ft.Row([ft.TextField(label="X1"), ft.TextField(label="Y1"), ft.Checkbox(label="Apoio u1"), ft.Checkbox(label="Apoio v1"), ft.Checkbox(label="Apoio θ1", visible=False)]),
                             ft.Row([ft.TextField(label="X2"), ft.TextField(label="Y2"), ft.Checkbox(label="Apoio u2"), ft.Checkbox(label="Apoio v2"), ft.Checkbox(label="Apoio θ2", visible=False)]),
                             ft.Row([ft.TextField(label="k"), ft.TextField(label="L", visible=False), ft.TextField(label="EI", visible=False), ft.TextField(label="AE", visible=False)])])

    # known check
    check_input = ft.Row([
        ft.Column([
            ft.Row([ft.Checkbox(label="u1 conhecido", value=False, on_change=gl_check_box_change, visible=True),  ft.TextField(label="Deslocamento", visible=False)]),
            ft.Row([ft.Checkbox(label="v1 conhecido", value=False, on_change=gl_check_box_change, visible=True),  ft.TextField(label="Deslocamento", visible=False)]),
            ft.Row([ft.Checkbox(label="θ1 conhecido", value=False, on_change=gl_check_box_change, visible=False), ft.TextField(label="Radianos",     visible=False)]),
            ft.Row([ft.Checkbox(label="u2 conhecido", value=False, on_change=gl_check_box_change, visible=True),  ft.TextField(label="Deslocamento", visible=False)]),
            ft.Row([ft.Checkbox(label="v2 conhecido", value=False, on_change=gl_check_box_change, visible=True),  ft.TextField(label="Deslocamento", visible=False)]),
            ft.Row([ft.Checkbox(label="θ2 conhecido", value=False, on_change=gl_check_box_change, visible=False), ft.TextField(label="Radianos",     visible=False)])
                             ]),
        ft.Column([
            ft.Row([ft.Checkbox(label="Fu1", value=False, on_change=f_check_box_change, visible=True),  ft.TextField(label="F (N)",  visible=False)]),
            ft.Row([ft.Checkbox(label="Fv1", value=False, on_change=f_check_box_change, visible=True),  ft.TextField(label="F (N)",  visible=False)]),
            ft.Row([ft.Checkbox(label="Fθ1", value=False, on_change=f_check_box_change, visible=False), ft.TextField(label="T (Nm)", visible=False)]),
            ft.Row([ft.Checkbox(label="Fu2", value=False, on_change=f_check_box_change, visible=True),  ft.TextField(label="F (N)",  visible=False)]),
            ft.Row([ft.Checkbox(label="Fv2", value=False, on_change=f_check_box_change, visible=True),  ft.TextField(label="F (N)",  visible=False)]),
            ft.Row([ft.Checkbox(label="Fθ2", value=False, on_change=f_check_box_change, visible=False), ft.TextField(label="T (Nm)", visible=False)])
                        ])], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    # Done button
    button = ft.ElevatedButton(text="Add", on_click=button_click)

    x1 = lambda: input_field.controls[0].controls[0].value
    y1 = lambda: input_field.controls[0].controls[1].value
    x2 = lambda: input_field.controls[1].controls[0].value
    y2 = lambda: input_field.controls[1].controls[1].value
    k = lambda: input_field.controls[2].controls[0].value
    l = lambda: input_field.controls[2].controls[1].value
    ei = lambda: input_field.controls[2].controls[2].value
    ae = lambda: input_field.controls[2].controls[3].value

    apoio_u1 = lambda: input_field.controls[0].controls[2].value
    apoio_v1 = lambda: input_field.controls[0].controls[3].value
    apoio_θ1 = lambda: input_field.controls[0].controls[4].value
    apoio_u2 = lambda: input_field.controls[1].controls[2].value
    apoio_v2 = lambda: input_field.controls[1].controls[3].value
    apoio_θ2 = lambda: input_field.controls[1].controls[4].value

    checkbox_u1 = lambda: check_input.controls[0].controls[0].controls[0].value
    checkbox_v1 = lambda: check_input.controls[0].controls[1].controls[0].value
    checkbox_θ1 = lambda: check_input.controls[0].controls[2].controls[0].value
    checkbox_u2 = lambda: check_input.controls[0].controls[3].controls[0].value
    checkbox_v2 = lambda: check_input.controls[0].controls[4].controls[0].value
    checkbox_θ2 = lambda: check_input.controls[0].controls[5].controls[0].value

    input_u1 = lambda: check_input.controls[0].controls[0].controls[1].value
    input_v1 = lambda: check_input.controls[0].controls[1].controls[1].value
    input_θ1 = lambda: check_input.controls[0].controls[2].controls[1].value
    input_u2 = lambda: check_input.controls[0].controls[3].controls[1].value
    input_v2 = lambda: check_input.controls[0].controls[4].controls[1].value
    input_θ2 = lambda: check_input.controls[0].controls[5].controls[1].value

    checkbox_fu1 = lambda: check_input.controls[1].controls[0].controls[0].value
    checkbox_fv1 = lambda: check_input.controls[1].controls[1].controls[0].value
    checkbox_tθ1 = lambda: check_input.controls[1].controls[2].controls[0].value
    checkbox_fu2 = lambda: check_input.controls[1].controls[3].controls[0].value
    checkbox_fv2 = lambda: check_input.controls[1].controls[4].controls[0].value
    checkbox_tθ2 = lambda: check_input.controls[1].controls[5].controls[0].value

    input_fu1 = lambda: check_input.controls[1].controls[0].controls[1].value
    input_fv1 = lambda: check_input.controls[1].controls[1].controls[1].value
    input_tθ1 = lambda: check_input.controls[1].controls[2].controls[1].value
    input_fu2 = lambda: check_input.controls[1].controls[3].controls[1].value
    input_fv2 = lambda: check_input.controls[1].controls[4].controls[1].value
    input_tθ2 = lambda: check_input.controls[1].controls[5].controls[1].value

    # Main page layout
    page.add(dropdown,
             ft.Text("Pos"),
             input_field,
             check_input,
             button)


def run():
    ft.app(target=inp_page)
    return elementos, nos
