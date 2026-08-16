import customtkinter as ctk
from PIL import Image
from Interfaces.TelaInicial import criar_tela_inicial
from Utils.Tema import (
    criar_fundo_espacial,
    criar_painel,
    estilizar_botao_primario,
    COR_NEON,
    COR_TEXTO_FRACO,
    FONTE_TITULO,
    FONTE_SUBTITULO,
    FONTE_TEXTO,
)

# Configurações iniciais do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

Main = ctk.CTk()
Main.title("Space Editor: Magistrosas Edition")

# Esconde a janela até ela já estar maximizada
Main.withdraw()


def maximizar_janela():
    try:
        # Mantém as bordas e o padrão do Windows
        Main.state('zoomed')
    except Exception:
        # Fallback pra sistemas onde 'zoomed' não existe (ex.: Linux/Mac)
        largura = Main.winfo_screenwidth()
        altura = Main.winfo_screenheight()
        Main.geometry(f"{largura}x{altura}+0+0")
    Main.deiconify()


# Agenda a maximização pro início do loop de eventos, já com a janela pronta
Main.after(0, maximizar_janela)

# Fundo espacial ocupando a janela inteira (degradê + estrelas cintilantes)
fundo = criar_fundo_espacial(Main)
fundo.pack(fill="both", expand=True)

# Painel central "flutuante" com o splash
painel_splash = criar_painel(fundo, relx=0.5, rely=0.5, largura=520, altura=460)

# Moldura da imagem (borda neon dando um efeito de "porta-retrato" espacial)
moldura_imagem = ctk.CTkFrame(
    painel_splash, fg_color="transparent",
    border_color=COR_NEON, border_width=2, corner_radius=24,
)
moldura_imagem.pack(pady=(36, 20))

try:
    img_pil = Image.open("ellie_espaco.png")

    largura_orig, altura_orig = img_pil.size
    altura_nova = 250  
    proporcao = largura_orig / altura_orig
    largura_nova = int(altura_nova * proporcao)

    img_ctk = ctk.CTkImage(light_image=img_pil, dark_image=img_pil, size=(largura_nova, altura_nova))
    label_imagem = ctk.CTkLabel(moldura_imagem, text="", image=img_ctk)
    label_imagem.pack(padx=8, pady=8)
except FileNotFoundError:
    # Se a imagem não estiver na pasta, mostra um foguete no lugar dela
    label_imagem = ctk.CTkLabel(moldura_imagem, text="🚀", font=("Segoe UI Emoji", 90))
    label_imagem.pack(padx=32, pady=32)
    print("Aviso: Imagem não encontrada. Salve o arquivo como 'ellie_espaco.png'")

titulo = ctk.CTkLabel(painel_splash, text="SPACE EDITOR", font=FONTE_TITULO, text_color=COR_NEON)
titulo.pack(pady=(0, 2))

subtitulo = ctk.CTkLabel(painel_splash, text="Magistrosas Edition", font=FONTE_SUBTITULO, text_color=COR_TEXTO_FRACO)
subtitulo.pack(pady=(0, 22))

Label_carregando = ctk.CTkLabel(painel_splash, text="Iniciando sistemas...", font=FONTE_TEXTO, text_color=COR_NEON)
Label_carregando.pack(pady=6)

barra_progresso = ctk.CTkProgressBar(
    painel_splash, orientation="horizontal", mode="indeterminate",
    progress_color=COR_NEON, width=320,
)
barra_progresso.pack(pady=10)
barra_progresso.start()


# Transicionar para a Tela Inicial
def mostrar_tela_inicial():
    # Destroi o fundo (canvas + painel) de uma vez, limpando a tela de carregamento
    fundo.destroy()

    # Cria e exibe a Tela Inicial ocupando a tela toda
    tela_inicial = criar_tela_inicial(Main)
    tela_inicial.pack(fill="both", expand=True)


# Agenda a troca após 3 segundos
Main.after(3000, mostrar_tela_inicial)

Main.mainloop()