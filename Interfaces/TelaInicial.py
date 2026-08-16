import customtkinter as ctk
from Interfaces.TelaImportacao import criar_tela_importacao
from Utils.Tema import (
    criar_fundo_espacial,
    criar_painel,
    estilizar_botao_primario,
    COR_NEON,
    COR_TEXTO_FRACO,
    FONTE_TITULO,
    FONTE_TEXTO,
)


def criar_tela_inicial(janela_mestre):
    # Fundo espacial cobrindo a janela toda
    fundo = criar_fundo_espacial(janela_mestre)

    # Painel central com o texto de boas-vindas
    painel = criar_painel(fundo, relx=0.5, rely=0.5, largura=560, altura=340)

    titulo = ctk.CTkLabel(
        painel, text="🛰  SPACE EDITOR", font=FONTE_TITULO, text_color=COR_NEON
    )
    titulo.pack(pady=(56, 10))

    subtitulo = ctk.CTkLabel(
        painel,
        text="Seja bem-vindo(a) ao editor de fotos do espaço",
        font=FONTE_TEXTO,
        text_color=COR_TEXTO_FRACO,
    )
    subtitulo.pack(pady=(0, 30))

    # Função para transicionar para a Tela de Importação
    def ir_para_importacao():
        fundo.pack_forget()
        tela_importacao = criar_tela_importacao(janela_mestre)
        tela_importacao.pack(fill="both", expand=True)

    # Botão para ir para a Tela de Importação
    botao = ctk.CTkButton(painel, text="Entrar", command=ir_para_importacao, width=200, height=44)
    estilizar_botao_primario(botao)
    botao.pack(pady=10)

    # Resultado (opcional, pode ser usado para mensagens futuras)
    resultado = ctk.CTkLabel(painel, text="", text_color=COR_TEXTO_FRACO)
    resultado.pack()

    return fundo