import customtkinter as ctk
from tkinter import filedialog
from Models.OpenCv import tirar_foto_webcam
from Interfaces.TelaEdicao import criar_tela_edicao
from Utils.Tema import (
    criar_fundo_espacial,
    criar_painel,
    estilizar_botao_primario,
    estilizar_botao_secundario,
    COR_NEON,
    FONTE_SECAO,
)


def criar_tela_importacao(janela_mestre):
    fundo = criar_fundo_espacial(janela_mestre)
    painel = criar_painel(fundo, relx=0.5, rely=0.5, largura=560, altura=380)

    # Função interna que esconde a tela atual e chama a de edição
    def ir_para_edicao(caminho_imagem):
        if caminho_imagem:
            fundo.pack_forget()
            tela_edicao = criar_tela_edicao(janela_mestre, caminho_imagem)
            tela_edicao.pack(fill="both", expand=True)

    label = ctk.CTkLabel(
        painel, text="📡  Escolha uma forma de importação",
        font=FONTE_SECAO, text_color=COR_NEON,
    )
    label.pack(pady=(56, 34))

    # Abrir arquivo usando filedialog
    def selecionar_arquivo():
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp")]
        )

        if caminho_arquivo:
            print(f"Arquivo selecionado: {caminho_arquivo}")
            ir_para_edicao(caminho_arquivo)

    btn_abrir_arquivo = ctk.CTkButton(
        painel, text="Selecionar Arquivo", command=selecionar_arquivo, width=260, height=46
    )
    estilizar_botao_primario(btn_abrir_arquivo)
    btn_abrir_arquivo.pack(pady=10)

    # Abrir webcam usando OpenCV
    def abrir_webcam():
        caminho_foto = tirar_foto_webcam()
        if caminho_foto:  # Só avança se a pessoa realmente tirou a foto
            print(f"Foto tirada e salva em: {caminho_foto}")
            ir_para_edicao(caminho_foto)

    btn_webcam = ctk.CTkButton(
        painel, text="Abrir Câmera", command=abrir_webcam, width=260, height=46
    )
    estilizar_botao_secundario(btn_webcam)
    btn_webcam.pack(pady=10)

    return fundo