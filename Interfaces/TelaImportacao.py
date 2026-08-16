import customtkinter as ctk
from tkinter import filedialog
from Models.OpenCv import tirar_foto_webcam
from Interfaces.TelaEdicao import criar_tela_edicao # ADICIONADO: Import da tela de edição

def criar_tela_importacao(janela_mestre):
    
    frame_importacao = ctk.CTkFrame(master=janela_mestre) 

    # ADICIONADO: Função interna que esconde a tela atual e chama a de edição
    def ir_para_edicao(caminho_imagem):
        if caminho_imagem:
            frame_importacao.pack_forget() 
            tela_edicao = criar_tela_edicao(janela_mestre, caminho_imagem) 
            tela_edicao.pack(pady=20, fill="both", expand=True)

    # Aqui os elementos vão dentro do frame_importacao, e não soltos

    label = ctk.CTkLabel(frame_importacao, text="Escolha uma forma de importação", font=("Arial", 24))
    label.pack(pady=20)
        
    #Abrir arquivo usando filedialog

    def selecionar_arquivo():
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp")]
        )
        
        if caminho_arquivo:
            print(f"Arquivo selecionado: {caminho_arquivo}")
            ir_para_edicao(caminho_arquivo) # ADICIONADO: Manda a foto pro editor
            

    btn_abrir_arquivo = ctk.CTkButton(frame_importacao, text="Selecionar Arquivo", command=selecionar_arquivo)
    btn_abrir_arquivo.pack(pady=10)

    #Abrir webcam usando OpenCV

    def abrir_webcam():
        caminho_foto = tirar_foto_webcam()
        if caminho_foto: # ADICIONADO: Só avança se a pessoa realmente tirou a foto
            print(f"Foto tirada e salva em: {caminho_foto}")
            ir_para_edicao(caminho_foto) # ADICIONADO: Manda a foto pro editor

    #Botao para abrir a webcam
        
    btn_webcam = ctk.CTkButton(frame_importacao, text="Abrir Câmera", command=abrir_webcam)
    btn_webcam.pack(pady=10)

    
    return frame_importacao