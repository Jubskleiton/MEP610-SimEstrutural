import flet as ft


def main(page: ft.Page):
    def button_click(e):
        popup.open = True  # show popup
        page.update()

    def close_dlg(e):
        popup.open = False
        page.update()

    def dropdown_changed(e):
        match dropdown.value:
            case "Mola":
                print("Mola")
            case  "Viga":
                print("Viga")
            case "Barra":
                print("Barra")
            case _:
                print("????????????????")

    # main page
    # select dropdown
    dropdown = ft.Dropdown(width=200,
                           options=[ft.dropdown.Option("Mola"),
                                    ft.dropdown.Option("Viga"),
                                    ft.dropdown.Option("Barra")],
                           value="Mola",
                           on_change=dropdown_changed)
    # pos input
    input_field = ft.Column([ft.Row([ft.TextField(label="X1"), ft.TextField(label="Y1")]),
                             ft.Row([ft.TextField(label="X2"), ft.TextField(label="Y2")])])

    # known check
    check_input = ft.Row([ft.Checkbox(label="1 conhecido", value=False), ft.Checkbox(label="2 conhecido", value=False)])
    # Done button
    button = ft.ElevatedButton(text="Ok", on_click=button_click)

    image = ft.Container()

    # popup
    popup = ft.AlertDialog(
        title=ft.Text("PopUp Title"),
        actions=[
            ft.TextField(label="popup message"),
            ft.ElevatedButton(text="close", on_click=close_dlg)
        ]
    )
    # add popup to the page
    page.dialog = popup

    # Main page layout
    page.add(ft.Row([dropdown, check_input]),
             ft.Text("Pos"),
             input_field,
             button)


ft.app(target=main)
