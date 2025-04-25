import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

class User():
    def __init__(self, profissao, salario):
        self.profissao = profissao
        self.salario = salario

def main(page: ft.Page):
    # Configurações
    page.title = "Trabalho"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []
    def salvar_tudo(e):
        if input_profissao.value == "" and input_salario.value == "":
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_erro)
            # Vai abrir a mensagem
            msg_erro.open = True
            page.update()
        else:
            obj_user = User(
                profissao=input_profissao.value,
                salario=input_salario.value,
            )
            # Adiciona o valor de input_profissão e input_salário na lista
            lista.append(obj_user)
            input_profissao.value = ""
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_sucesso)
            # Vai abrir a mensagem
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        lv_nome.controls.clear()
        for use in lista:
            lv_nome.controls.append(
                ft.Text(value= f'Profissão: {use.profissao} - Salário: {use.salario}')
            )
        page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_profissao,
                    input_salario,
                    # Irá salvar os Nomes
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_tudo(e),
                    ),
                        # Irá mostrar os nomes
                        ft.Button(
                            text="Exibir lista",
                            on_click=lambda _: page.go("/segunda"),
                        )
                ],
            )
        )
        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("SALVOU"),
        bgcolor=Colors.GREEN
    )
    msg_erro = ft.SnackBar(
        content=ft.Text("ERRO"),
        bgcolor=Colors.RED
    )
    input_profissao = ft.TextField(label="Profissão")
    input_salario = ft.TextField(label="Salário")

    lv_nome = ft.ListView(
        height=500
    )

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)