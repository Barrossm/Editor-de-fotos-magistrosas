import customtkinter as ctk
from PIL import Image  
from Utils.Tema import (
    criar_fundo_espacial,
    criar_painel_cheio,
    estilizar_botao_secundario,
    estilizar_botao_perigo,
    COR_NEON,
    COR_BORDA,
    FONTE_SECAO,
)


def criar_tela_edicao(janela_mestre, caminho_imagem):
    fundo = criar_fundo_espacial(janela_mestre)
    painel = criar_painel_cheio(fundo, margem=40)

    # DIVIDINDO A TELA (Menu Lateral e Área da Foto)

    frame_menu = ctk.CTkFrame(
        painel, width=220, fg_color="#0a0c1f",
        corner_radius=14, border_width=1, border_color=COR_BORDA,
    )
    frame_menu.pack(side="left", fill="y", padx=(20, 10), pady=20)
    frame_menu.pack_propagate(False)

    frame_imagem = ctk.CTkFrame(painel, fg_color="transparent")
    frame_imagem.pack(side="right", fill="both", expand=True, padx=(10, 20), pady=20)

    # "Viewport" com moldura neon ao redor da foto (efeito janela de nave)
    # Preenche o espaço disponível — o tamanho da foto dentro dela se
    # recalcula sozinho sempre que a janela é redimensionada.
    moldura = ctk.CTkFrame(
        frame_imagem, fg_color="#05060f",
        border_color=COR_NEON, border_width=2, corner_radius=16,
    )
    moldura.pack(fill="both", expand=True)

    # Lendo o arquivo que veio da tela de importação 
    img_pil_original = Image.open(caminho_imagem)

    label_foto = ctk.CTkLabel(moldura, text="")
    label_foto.pack(padx=14, pady=14, expand=True)

    _agendamento = {"id": None}

    def calcular_tamanho_ajustado(largura_max, altura_max):
        largura_orig, altura_orig = img_pil_original.size
        # Nunca deixa passar do espaço disponível
        proporcao = min(largura_max / largura_orig, altura_max / altura_orig)
        # nunca aumenta a foto além do tamanho original (evita pixelizar)
        proporcao = min(proporcao, 1)
        nova_largura = max(int(largura_orig * proporcao), 1)
        nova_altura = max(int(altura_orig * proporcao), 1)
        return nova_largura, nova_altura

    def redesenhar_imagem():
        largura_disponivel = max(moldura.winfo_width() - 28, 100)
        altura_disponivel = max(moldura.winfo_height() - 28, 100)
        nova_largura, nova_altura = calcular_tamanho_ajustado(largura_disponivel, altura_disponivel)

        img_ctk = ctk.CTkImage(
            light_image=img_pil_original, dark_image=img_pil_original,
            size=(nova_largura, nova_altura),
        )
        label_foto.configure(image=img_ctk)
        label_foto.image = img_ctk  # evita garbage collection

    def ao_redimensionar(event=None):
        # Pequeno debounce: só redesenha a imagem 80ms depois do último
        # evento de redimensionamento, pra não recriar a imagem a cada pixel
        if _agendamento["id"] is not None:
            moldura.after_cancel(_agendamento["id"])
        _agendamento["id"] = moldura.after(80, redesenhar_imagem)

    moldura.bind("<Configure>", ao_redimensionar)

    # Botões de Filtros

    titulo = ctk.CTkLabel(frame_menu, text="🎛  FILTROS", font=FONTE_SECAO, text_color=COR_NEON)
    titulo.pack(pady=(30, 20), padx=20)

    # Funções do OpenCV (comandos ainda não conectados aos botões, só placeholder por enquanto)

    btn_cinza = ctk.CTkButton(frame_menu, text="Escala de Cinza")
    estilizar_botao_secundario(btn_cinza)
    btn_cinza.pack(pady=10, padx=20, fill="x")

    btn_blur = ctk.CTkButton(frame_menu, text="Desfoque (Blur)")
    estilizar_botao_secundario(btn_blur)
    btn_blur.pack(pady=10, padx=20, fill="x")

    btn_bordas = ctk.CTkButton(frame_menu, text="Detectar Bordas")
    estilizar_botao_secundario(btn_bordas)
    btn_bordas.pack(pady=10, padx=20, fill="x")

    # BOTÃO DE VOLTAR

    def voltar():
        # 1. Esconde a tela de edição atual
        fundo.pack_forget()

        # 2. Importa a fábrica AQUI DENTRO pra evitar o loop infinito de importação
        from Interfaces.TelaImportacao import criar_tela_importacao

        # 3. Fabrica e joga a tela de importação de volta na janela
        tela_anterior = criar_tela_importacao(janela_mestre)
        tela_anterior.pack(fill="both", expand=True)

    btn_voltar = ctk.CTkButton(frame_menu, text="Voltar", command=voltar)
    estilizar_botao_perigo(btn_voltar)
    btn_voltar.pack(side="bottom", pady=20, padx=20, fill="x")

    return fundo