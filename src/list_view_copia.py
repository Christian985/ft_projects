import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors


# Main
def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

    # Salva as informações
    def salvar_nome(e):
        if input_nome.value == "":
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_erro)
            # Vai abrir a mensagem
            msg_erro.open = True
            page.update()
        else:
            # Adiciona o valor de input_nome na lista
            lista.append(input_nome.value)
            input_nome.value = ""
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_sucesso)
            # Vai abrir a mensagem
            msg_sucesso.open = True
            page.update()
    # FIM do salvamento

    # Vai exibir a lista
    def exibir_lista(e):
        lv_nome.controls.clear()
        for nome in lista:
            lv_nome.controls.append(
                ft.Text(value=nome)
            )
        page.update()

    # FIM da exibição da lista

    # Gerencia o caminho das rotas
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(  # Primeira Página
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    # Irá salvar os Nomes
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_nome(e),
                    ),
                    # Irá mostrar os Nomes
                    ft.Button(
                        text="Exibir lista",
                        on_click=lambda _: page.go("/segunda"),
                    )
                ],
            )
        )
        # Segunda Página
        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda Tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,
                        ft.FloatingActionButton(text="+"),
                    ],
                )
            )
        page.update()

    # FIM da Transição de Páginas

    # Configura a seta para voltar
    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # FIM da seta de Voltar

    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("SALVOU"),
        bgcolor=Colors.GREEN
    )
    msg_erro = ft.SnackBar(
        content=ft.Text("ERRO"),
        bgcolor=Colors.RED
    )
    input_nome = ft.TextField(label="Nome")

    lv_nome = ft.ListView(
        height=500
    )
    # FIM dos Componentes

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)
    # FIM dos Eventos


# Comando que executa o Aplicativo
# Deve estar sempre colado na linha
ft.app(main)
