import customtkinter as ctk
from Interfaces.TelaInicial import criar_tela_inicial
from Interfaces.TelaImportacao import criar_tela_importacao

# Configurações iniciais do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

Main = ctk.CTk()
Main.title("Editor de Fotos magistrosas")
Main.geometry("800x600")

# Tela de Carregamento
Label_carregando = ctk.CTkLabel(Main, text="Editor de Fotos magistrosas", font=("Arial", 24))
Label_carregando.pack(pady=220)

barra_progresso = ctk.CTkProgressBar(Main, orientation="horizontal", mode="indeterminate")
barra_progresso.pack(pady=5)
barra_progresso.start() 

# Transicionar para a Tela Inicial
def mostrar_tela_inicial():
   
    Label_carregando.pack_forget()
    barra_progresso.stop()
    barra_progresso.pack_forget()
    
    # Cria e exibe a Tela Inicial
    tela_inicial = criar_tela_inicial(Main)
    tela_inicial.pack(pady=20, fill="both", expand=True)


# 3. Agenda a troca após 3 segundos
Main.after(3000, mostrar_tela_inicial)

Main.mainloop() 