import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from models_profissao import Profissao, db_session


# Main
def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.WHITE
    page.window.width = 375
    page.window.height = 667

    # Funções
    # Salva as informações
    def salvar_nome(e):
        if input_nome.value == "" or input_cargo.value == "" or input_salario.value == "":
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_erro)
            # Vai abrir a mensagem
            msg_erro.open = True
            page.update()
        else:
            obj_user = Profissao(
                nome=input_nome.value,
                cargo=input_cargo.value,
                salario=input_salario.value,

            )
            # Adiciona o valor de input_nome na Lista
            input_nome.value = ""
            input_cargo.value = ""
            input_salario.value = ""
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
                    # Irá entrar na profissao
                    ft.Button(
                        text="Profissão",
                        on_click=lambda _: page.go('/profissao'),
                    ),
                ],
            )
        )
        # Profissão
        if page.route == "/profissao":
            page.views.append(
                View(
                    "/profissao",
                    [
                        AppBar(title=Text("Profissão"), bgcolor=Colors.PRIMARY_CONTAINER),
                        input_nome,
                        input_cargo,
                        input_salario,
                        # Irá salvar os Dados
                        ft.Button(
                            text="Salvar",
                            on_click=lambda _: salvar_nome(e),
                        ),
                        # Irá mostrar os Dados
                        ft.Button(
                            text="Voltar",
                            on_click=lambda _: page.go("/"),
                        )
                    ],
                )
            )
        # FIM da Profissão

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
    input_cargo = ft.TextField(label="Cargo")
    input_salario = ft.TextField(label="Salario")

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
