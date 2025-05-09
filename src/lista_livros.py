import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

# Classe do Usuário
class User:
    def __init__(self, livro, sinopse):
        self.livro = livro
        self.sinopse = sinopse

# Main
def main(page: ft.Page):
    # Configurações
    page.title = "Livros"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

    # Salva as informações
    def salvar_tudo(e):
        if input_livro.value == "" or input_sinopse.value == "":
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_erro)
            # Vai abrir a mensagem
            msg_erro.open = True
            page.update()
        else:
            obj_user = User(
                livro=input_livro.value,
                sinopse=input_sinopse.value,
            )
            # Adiciona o valor de input_livro e input_sinopse na Lista
            lista.append(obj_user)
            input_livro.value = ""
            input_sinopse.value = ""
            # Overlay vai apagar as mensagens anteriores
            page.overlay.append(msg_sucesso)
            # Vai abrir a mensagem
            msg_sucesso.open = True
            page.update()
    # FIM do salvamento

    # Exibe a Lista
    def exibir_lista(e):
        lv_nome.controls.clear()
        for use in lista:
            lv_nome.controls.append(
                ft.Text(value= f'livro: {use.livro} - Sinopse: {use.sinopse}')
            )
        page.update()
    # FIM da exibição da lista

    # Gerencia o caminho das rotas
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    # Primeira Página
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_livro,
                    input_sinopse,
                    # Irá salvar os conteúdos
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_tudo(e),
                    ),
                        # Irá mostrar os conteúdos
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
                        AppBar(title=Text("Livros e detalhes"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,
                    ],
                )
            )
        page.update()
    # FIM da Transsição de Páginas

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

    lv_nome = ft.ListView(
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