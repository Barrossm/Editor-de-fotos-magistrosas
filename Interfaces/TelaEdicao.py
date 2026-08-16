import customtkinter as ctk
from PIL import Image # O Tkinter precisa do Pillow para desenhar imagens na tela

def criar_tela_edicao(janela_mestre, caminho_imagem):
    frame_edicao = ctk.CTkFrame(master=janela_mestre)

    
    #  DIVIDINDO A TELA (Menu Lateral e Área da Foto)
    
    frame_menu = ctk.CTkFrame(frame_edicao, width=200, corner_radius=0)
    frame_menu.pack(side="left", fill="y")

    frame_imagem = ctk.CTkFrame(frame_edicao, fg_color="transparent")
    frame_imagem.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    
    # Lendo o arquivo que veio lá da tela de importação
    img_pil = Image.open(caminho_imagem)
    
    # Transformando no formato que o CustomTkinter entende
    img_ctk = ctk.CTkImage(light_image=img_pil, dark_image=img_pil, size=(500, 400))

    label_foto = ctk.CTkLabel(frame_imagem, text="", image=img_ctk)
    label_foto.pack(expand=True)

    
    # Botões de Filtros

    titulo = ctk.CTkLabel(frame_menu, text="Filtros", font=("Arial", 20, "bold"))
    titulo.pack(pady=20, padx=20)

    # Funções do OpenCV

    btn_cinza = ctk.CTkButton(frame_menu, text="Escala de Cinza")
    btn_cinza.pack(pady=10, padx=20)

    btn_blur = ctk.CTkButton(frame_menu, text="Desfoque (Blur)")
    btn_blur.pack(pady=10, padx=20)

    btn_bordas = ctk.CTkButton(frame_menu, text="Detectar Bordas")
    btn_bordas.pack(pady=10, padx=20)

   
    # BOTÃO DE VOLTAR

    def voltar():
        # 1. Esconde a tela de edição atual
        frame_edicao.pack_forget()
        
        # 2. Importa a fábrica AQUI DENTRO pra evitar o loop infinito de importação
        from Interfaces.TelaImportacao import criar_tela_importacao
        
        # 3. Fabrica e joga a tela de importação de volta na janela
        tela_anterior = criar_tela_importacao(janela_mestre)
        tela_anterior.pack(pady=20, fill="both", expand=True)

    btn_voltar = ctk.CTkButton(frame_menu, text="Voltar", fg_color="#8B0000", hover_color="#5C0000", command=voltar)
    btn_voltar.pack(side="bottom", pady=20, padx=20)

    return frame_edicao