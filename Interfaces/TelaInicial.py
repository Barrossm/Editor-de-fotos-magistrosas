import customtkinter as ctk
from Interfaces.TelaImportacao import criar_tela_importacao

def criar_tela_inicial(janela_mestre):

    # Cria o frame e coloca ele na janela_mestre
    frame_inicial = ctk.CTkFrame(master=janela_mestre)

    # Função para transicionar para a Tela de Importação
    def ir_para_importacao():
        frame_inicial.pack_forget() 
        tela_importacao = criar_tela_importacao(janela_mestre) 
        tela_importacao.pack(pady=20, fill="both", expand=True) 

    
    label = ctk.CTkLabel(frame_inicial, text="Seja bem-vindo ao editor de Fotos Magistrosas", font=("Arial", 24))
    label.pack(pady=20)

    # Botão para ir para a Tela de Importação
    botao = ctk.CTkButton(frame_inicial, text="Entrar", command=ir_para_importacao)
    botao.pack(pady=10)

    # Resultado (opcional, pode ser usado para mensagens futuras)
    resultado = ctk.CTkLabel(frame_inicial, text="")
    resultado.pack()

    return frame_inicial
