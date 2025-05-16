import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from models_livro import Livro, db_session


# Main
def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.WHITE
    page.window.width = 375
    page.window.height = 667

    # Funções
    # Salva as informações
    def salvar_livro(e):
        if input_livro.value == "" or input_sinopse.value == "":
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_erro)
            # Vai abrir a mensagem
            msg_erro.open = True
            page.update()
        else:
            obj_user = Livro(
                livro=input_livro.value,
                sinopse=input_sinopse.value,

            )
            # Adiciona o valor de input_livro e input_sinopse na Lista
            input_livro.value = ""
            input_sinopse.value = ""
            db_session.add(obj_user)
            db_session.commit()
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_sucesso)
            # Vai abrir a mensagem
            msg_sucesso.open = True
            page.update()

    # FIM do salvamento

    # FIM da exibição da lista

    # Gerencia o caminho das rotas
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(  # Primeira Página
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    # Irá entrar no livro
                    ft.Button(
                        text="Livros",
                        on_click=lambda _: page.go('/livro'),
                    ),
                ],
            )
        )
        # Livro
        if page.route == "/livro":
            page.views.append(
                View(
                    "/livro",
                    [
                        AppBar(title=Text("Livro"), bgcolor=Colors.PRIMARY_CONTAINER),
                        input_livro,
                        input_sinopse,
                        # Irá salvar os Dados
                        ft.Button(
                            text="Salvar",
                            on_click=lambda _: salvar_livro(e),
                        ),
                        # Irá mostrar os Dados
                        ft.Button(
                            text="Voltar",
                            on_click=lambda _: page.go("/"),
                        )
                    ],
                )
            )
        # FIM do Livro

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
    input_livro = ft.TextField(label="Livro")
    input_sinopse = ft.TextField(label="Sinopse")

    lv_livro = ft.ListView(
        height=500
    )
    # FIM dos Componentes

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)
    # FIM dos Eventos


# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
