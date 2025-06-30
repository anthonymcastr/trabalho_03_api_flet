import flet as ft
import requests
from telas.cad_produtos import cad_produtos
from telas.graf_marcas import graf_marcas
from telas.graf_caros import graf_caros
# npx json-server db.json (uso pra rodar a API na outra pasta)
API_URL = "http://localhost:3000/produtos"

# buscamos os produtos e geramos os cards
def buscar_produtos_local(termo):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        produtos = response.json()

        termo = termo.lower()
        filtrados = [p for p in produtos if termo in p["nome"].lower()]

        if not filtrados:
            return [ft.Text("Nenhum produto encontrado.")]

        total_valor = sum(p["quant"] * p["preco"] for p in filtrados)
        total_itens = len(filtrados)

        cards = [ 
            ft.Card(
                elevation=2,
                surface_tint_color=ft.Colors.BLUE_50,
                content=ft.ListTile(
                    title=ft.Text(p["nome"], color=ft.Colors.BLUE_900),
                    subtitle=ft.Text(f"Marca: {p['marca']} • Preço: R$ {p['preco']:.2f} • Quantidade: {p['quant']}", color=ft.Colors.BLUE_GREY_700),
                )
            )
            for p in filtrados
        ]

        # produtos encontrados e somatorio total
        cards.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(f"🔎 {total_itens} produto(s) encontrado(s)", size=16, color=ft.Colors.BLUE_800),
                    ft.Text(f"💰 Valor total em estoque: R$ {total_valor:,.2f}", size=18, weight="bold", color=ft.Colors.BLUE),
                ]),
                alignment=ft.alignment.center,
                padding=10,
            )
        )

        return cards

    except Exception as err:
        return [ft.Text(f"Erro ao buscar produtos: {err}", color=ft.Colors.RED)]

def main(page: ft.Page):
    page.title = "CK Informática - Estoque"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    snack = ft.SnackBar(
        content=ft.Text("", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE_300,
        open=False
    )
    page.snack_bar = snack
    page.overlay.append(snack)

    conteudo_dinamico = ft.Column()

    def buscar_produto(e):
        termo = campo_pesquisa.value.strip()
        if not termo:
            snack.content.value = "Digite um nome para buscar."
            snack.open = True
            page.update()
            return

        conteudo_dinamico.controls = buscar_produtos_local(termo)
        page.update()

    campo_pesquisa = ft.TextField(
        label="Pesquisar produto",
        expand=True,
        border_color=ft.Colors.BLUE,
        focused_border_color=ft.Colors.BLUE_700
    )

    linha_pesquisa = ft.Row([
        campo_pesquisa,
        ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.BLUE, on_click=buscar_produto),
    ])

    def navigate(e):
        rota = e.control.data
        if rota == "cad_produtos":
            conteudo_dinamico.controls = [cad_produtos(page)]
        elif rota == "graf_marcas":
            conteudo_dinamico.controls = [graf_marcas(page)]
        elif rota == "graf_caros":
            conteudo_dinamico.controls = [graf_caros(page)]
        page.update()

    nav_buttons = ft.Row([
        ft.ElevatedButton("Cadastro de Produtos", data="cad_produtos", on_click=navigate, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
        ft.ElevatedButton("Gráfico por Marcas", data="graf_marcas", on_click=navigate, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
        ft.ElevatedButton("Gráfico + Caros", data="graf_caros", on_click=navigate, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
    ], alignment=ft.MainAxisAlignment.CENTER)

    # Tela inicial
    conteudo_dinamico.controls = [cad_produtos(page)]

    page.add(
        ft.Column([
            ft.Text("CK Informática - Cadastro de Produtos", size=30, weight="bold", text_align="center", color=ft.Colors.BLUE_900),
            nav_buttons, # botões de navegação
            linha_pesquisa, # pesquisa que acrescentei 
            ft.Divider(color=ft.Colors.BLUE_200, thickness=2), 
            conteudo_dinamico
        ], scroll=ft.ScrollMode.AUTO)
    )

ft.app(target=main)
