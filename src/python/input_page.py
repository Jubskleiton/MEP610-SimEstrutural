import flet as ft


def inp_page(page: ft.Page):
    def button_click(e):
        match dropdown.value:
            case "Mola":
                if x1() and y1() and x2() and y2() and k() and (not checkbox_u1() or input_u1()) and (not checkbox_v1() or input_v1()) and (not checkbox_u2() or input_u2()) and (not checkbox_v2() or input_v2()):
                    print("pass")
                else:
                    print("falta")
            case "Viga":
                if x1() and y1() and x2() and y2() and (not checkbox_u1() or input_u1()) and (not checkbox_v1() or input_v1()) and (not checkbox_θ1() or input_θ1()) and (not checkbox_u2() or input_u2()) and (not checkbox_v2() or input_v2()) and (not checkbox_θ2() or input_θ2()) and l() and ei():
                    print("pass")
                else:
                    print("falta")
            case "Barra":
                if x1() and y1() and x2() and y2() and (not checkbox_u1() or input_u1()) and (not checkbox_v1() or input_v1()) and (not checkbox_u2() or input_u2()) and (not checkbox_v2() or input_v2()) and l() and ae():
                    print("pass")
                else:
                    print("falta")
            case "Portico":
                if x1() and y1() and x2() and y2() and (not checkbox_u1() or input_u1()) and (not checkbox_v1() or input_v1()) and (not checkbox_θ1() or input_θ1()) and (not checkbox_u2() or input_u2()) and (not checkbox_v2() or input_v2()) and (not checkbox_θ2() or input_θ2()) and l() and ei():
                    print("pass")
                else:
                    print("falta")

    def check_box_change(e):
        if checkbox_u1():
            check_input.controls[0].controls[1].visible = True   # input u1
        else:
            check_input.controls[0].controls[1].visible = False
        if checkbox_v1():
            check_input.controls[1].controls[1].visible = True   # input v1
        else:
            check_input.controls[1].controls[1].visible = False
        if checkbox_θ1():
            check_input.controls[2].controls[1].visible = True   # input θ1
        else:
            check_input.controls[2].controls[1].visible = False
        if checkbox_u2():
            check_input.controls[3].controls[1].visible = True   # input u2
        else:
            check_input.controls[3].controls[1].visible = False
        if checkbox_v2():
            check_input.controls[4].controls[1].visible = True   # input v2
        else:
            check_input.controls[4].controls[1].visible = False
        if checkbox_θ2():
            check_input.controls[5].controls[1].visible = True   # input θ2
        else:
            check_input.controls[5].controls[1].visible = False
        page.update()

    def dropdown_changed(e):
        match dropdown.value:
            case "Mola":
                input_field.controls[2].controls[0].visible = True   # K
                input_field.controls[2].controls[1].visible = False  # L
                input_field.controls[2].controls[2].visible = False  # EI
                input_field.controls[2].controls[3].visible = False  # AE

                check_input.controls[2].controls[0].visible = False  # checkbox θ1
                check_input.controls[2].controls[1].visible = False  # input θ1
                check_input.controls[5].controls[0].visible = False  # checkbox θ2
                check_input.controls[5].controls[1].visible = False  # input θ2
            case  "Viga":
                input_field.controls[2].controls[0].visible = False  # K
                input_field.controls[2].controls[1].visible = True   # L
                input_field.controls[2].controls[2].visible = True   # EI
                input_field.controls[2].controls[3].visible = False  # AE

                check_input.controls[2].controls[0].visible = True   # checkbox θ1
                check_input.controls[5].controls[0].visible = True   # checkbox θ2
            case "Barra":
                input_field.controls[2].controls[0].visible = False  # K
                input_field.controls[2].controls[1].visible = True   # L
                input_field.controls[2].controls[2].visible = False  # EI
                input_field.controls[2].controls[3].visible = True   # AE

                check_input.controls[2].controls[0].visible = False  # checkbox θ1
                check_input.controls[2].controls[1].visible = False  # input θ1
                check_input.controls[5].controls[0].visible = False  # checkbox θ2
                check_input.controls[5].controls[1].visible = False  # input θ2
            case "Portico":
                input_field.controls[2].controls[0].visible = False  # K
                input_field.controls[2].controls[1].visible = True   # L
                input_field.controls[2].controls[2].visible = True   # EI
                input_field.controls[2].controls[3].visible = False  # AE

                check_input.controls[2].controls[0].visible = True   # checkbox θ1
                check_input.controls[2].controls[1].visible = False  # input θ1
                check_input.controls[5].controls[0].visible = True   # checkbox θ2
                check_input.controls[5].controls[1].visible = False  # input θ2
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
    input_field = ft.Column([ft.Row([ft.TextField(label="X1"), ft.TextField(label="Y1")]),
                             ft.Row([ft.TextField(label="X2"), ft.TextField(label="Y2")]),
                             ft.Row([ft.TextField(label="k"), ft.TextField(label="L", visible=False), ft.TextField(label="EI", visible=False), ft.TextField(label="AE", visible=False)])])

    # known check
    check_input = ft.Column([ft.Row([ft.Checkbox(label="u1 conhecido", value=False, on_change=check_box_change), ft.TextField(label="Deslocamento", visible=False)]),
                             ft.Row([ft.Checkbox(label="v1 conhecido", value=False, on_change=check_box_change), ft.TextField(label="Deslocamento", visible=False)]),
                             ft.Row([ft.Checkbox(label="θ1 conhecido", value=False, on_change=check_box_change, visible=False), ft.TextField(label="Radianos", visible=False)]),
                             ft.Row([ft.Checkbox(label="u2 conhecido", value=False, on_change=check_box_change), ft.TextField(label="Deslocamento", visible=False)]),
                             ft.Row([ft.Checkbox(label="v2 conhecido", value=False, on_change=check_box_change), ft.TextField(label="Deslocamento", visible=False)]),
                             ft.Row([ft.Checkbox(label="θ2 conhecido", value=False, on_change=check_box_change, visible=False), ft.TextField(label="Radianos", visible=False)])
                             ])
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

    checkbox_u1 = lambda: check_input.controls[0].controls[0].value
    checkbox_v1 = lambda: check_input.controls[1].controls[0].value
    checkbox_θ1 = lambda: check_input.controls[2].controls[0].value
    checkbox_u2 = lambda: check_input.controls[3].controls[0].value
    checkbox_v2 = lambda: check_input.controls[4].controls[0].value
    checkbox_θ2 = lambda: check_input.controls[5].controls[0].value

    input_u1 = lambda: check_input.controls[0].controls[1].value
    input_v1 = lambda: check_input.controls[1].controls[1].value
    input_θ1 = lambda: check_input.controls[2].controls[1].value
    input_u2 = lambda: check_input.controls[3].controls[1].value
    input_v2 = lambda: check_input.controls[4].controls[1].value
    input_θ2 = lambda: check_input.controls[5].controls[1].value

    # Main page layout
    page.add(dropdown,
             ft.Text("Pos"),
             input_field,
             check_input,
             button)


ft.app(target=inp_page)
