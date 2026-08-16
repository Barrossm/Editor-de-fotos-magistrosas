"""
Paleta de cores, fontes e componentes visuais compartilhados do Space Editor.
Centralizar tudo aqui evita ficar copiando cor por cor em cada tela.
"""

import random
import tkinter as tk
import customtkinter as ctk

# ---------- PALETA "ESPAÇO PROFUNDO" ----------
COR_FUNDO_TOPO = "#05060f"      # quase preto, com um azul bem escuro
COR_FUNDO_BASE = "#10132b"      # azul marinho profundo (degradê)
COR_PAINEL = "#0d0f24"          # fundo dos cards/painéis
COR_BORDA = "#2a2f5c"           # borda sutil de elementos internos

COR_NEON = "#00ffcc"            # ciano neon (ação principal)
COR_NEON_HOVER = "#00cca3"
COR_ROXO = "#b967ff"            # roxo nebulosa (ações secundárias)
COR_ROXO_HOVER = "#9a4de0"
COR_PERIGO = "#ff5470"          # vermelho/rosa (voltar / sair)
COR_PERIGO_HOVER = "#c9314f"

COR_TEXTO = "#e8e8ff"
COR_TEXTO_FRACO = "#9296c2"

# ---------- FONTES ----------
FONTE_TITULO = ("Consolas", 34, "bold")     # título grande (splash)
FONTE_SECAO = ("Consolas", 22, "bold")      # cabeçalhos de seção
FONTE_SUBTITULO = ("Consolas", 16)          # texto de apoio
FONTE_TEXTO = ("Consolas", 14)              # texto corrido
FONTE_BOTAO = ("Consolas", 14, "bold")      # texto dos botões


def criar_fundo_espacial(janela_mestre, num_estrelas=140):
    """
    Cria um Canvas que preenche a tela toda, com um degradê espacial
    e um campo de estrelas cintilantes. Retorna o Canvas — que funciona
    como container normal (dá pra chamar .pack() / .pack_forget() nele).
    """
    canvas = tk.Canvas(janela_mestre, highlightthickness=0, bd=0, bg=COR_FUNDO_TOPO)

    def desenhar_fundo(event=None):
        canvas.delete("fundo")
        largura = canvas.winfo_width()
        altura = canvas.winfo_height()
        if largura < 2 or altura < 2:
            return

        # Degradê vertical (linhas horizontais interpoladas do topo pra base)
        passos = 60
        r1, g1, b1 = 5, 6, 15
        r2, g2, b2 = 16, 19, 43
        for i in range(passos):
            cor = "#%02x%02x%02x" % (
                int(r1 + (r2 - r1) * (i / passos)),
                int(g1 + (g2 - g1) * (i / passos)),
                int(b1 + (b2 - b1) * (i / passos)),
            )
            y0 = int(altura * i / passos)
            y1 = int(altura * (i + 1) / passos)
            canvas.create_rectangle(0, y0, largura, y1, fill=cor, outline="", tags="fundo")

        # Campo de estrelas
        canvas.estrelas = []
        for _ in range(num_estrelas):
            x = random.randint(0, largura)
            y = random.randint(0, altura)
            tamanho = random.choice([1, 1, 1, 2])
            estrela = canvas.create_oval(
                x, y, x + tamanho, y + tamanho, fill=COR_TEXTO, outline="", tags="fundo"
            )
            canvas.estrelas.append(estrela)

    def cintilar():
        if not canvas.winfo_exists():
            return
        for estrela in getattr(canvas, "estrelas", []):
            if random.random() < 0.06:
                cor = random.choice([COR_TEXTO, COR_TEXTO_FRACO, COR_NEON])
                canvas.itemconfig(estrela, fill=cor)
        canvas.after(400, cintilar)

    canvas.bind("<Configure>", desenhar_fundo)
    canvas.after(500, cintilar)
    return canvas


def criar_painel(canvas, relx=0.5, rely=0.5, largura=600, altura=420, **kwargs_frame):
    """
    Cria um CTkFrame "flutuante" (card com borda neon), de tamanho fixo,
    centralizado sobre o fundo espacial. Ideal para telas de conteúdo
    curto (splash, menus).
    """
    painel = ctk.CTkFrame(
        canvas,
        fg_color=COR_PAINEL,
        border_color=COR_NEON,
        border_width=2,
        corner_radius=18,
        width=largura,
        height=altura,
        **kwargs_frame,
    )
    painel.pack_propagate(False)

    item_id = canvas.create_window(0, 0, anchor="center", window=painel)

    def posicionar(event=None):
        canvas.coords(item_id, canvas.winfo_width() * relx, canvas.winfo_height() * rely)

    canvas.bind("<Configure>", lambda e: posicionar(), add="+")
    canvas.after(50, posicionar)
    return painel


def criar_painel_cheio(canvas, margem=40, **kwargs_frame):
    """
    Painel que ocupa quase toda a tela (com uma margem), redimensionando
    junto com a janela. Ideal para telas de conteúdo denso (ex.: edição).
    """
    painel = ctk.CTkFrame(
        canvas,
        fg_color=COR_PAINEL,
        border_color=COR_NEON,
        border_width=2,
        corner_radius=18,
        **kwargs_frame,
    )
    item_id = canvas.create_window(margem, margem, anchor="nw", window=painel)

    def redimensionar(event=None):
        largura = max(canvas.winfo_width() - margem * 2, 10)
        altura = max(canvas.winfo_height() - margem * 2, 10)
        canvas.coords(item_id, margem, margem)
        canvas.itemconfig(item_id, width=largura, height=altura)

    canvas.bind("<Configure>", lambda e: redimensionar(), add="+")
    canvas.after(50, redimensionar)
    return painel


def estilizar_botao_primario(botao):
    """Botão de ação principal — preenchido em ciano neon."""
    botao.configure(
        fg_color=COR_NEON,
        hover_color=COR_NEON_HOVER,
        text_color="#02110d",
        font=FONTE_BOTAO,
        corner_radius=10,
        border_width=0,
    )


def estilizar_botao_secundario(botao):
    """Botão de ação secundária — contorno roxo, fundo transparente."""
    botao.configure(
        fg_color="transparent",
        hover_color="#1a1e40",
        text_color=COR_ROXO,
        border_color=COR_ROXO,
        border_width=2,
        font=FONTE_BOTAO,
        corner_radius=10,
    )


def estilizar_botao_perigo(botao):
    """Botão de ação destrutiva/voltar — vermelho-rosa."""
    botao.configure(
        fg_color=COR_PERIGO,
        hover_color=COR_PERIGO_HOVER,
        text_color="#1a0007",
        font=FONTE_BOTAO,
        corner_radius=10,
        border_width=0,
    )
