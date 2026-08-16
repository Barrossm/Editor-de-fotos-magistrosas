# 🚀 Space Editor: Magistrosas Edition

Um editor de imagens desenvolvido em Python com foco em aplicar conceitos práticos de **Visão Computacional** e **Fotografia Computacional**. O projeto utiliza uma interface gráfica com tema espacial para capturar e processar pixels, servindo como laboratório para a criação de filtros e manipulação de matrizes de imagens.

Este projeto faz parte dos meus estudos e desenvolvimentos práticos no bacharelado em Ciência da Computação (BCC) na UFRPE, juntamente com meus aprendizados no curso de Fotografia Computacional no CIn da UFPE.

## 🌌 Interface Gráfica

O app inteiro segue uma identidade visual de "espaço profundo":

- **Fundo animado:** degradê azul-marinho → preto com um campo de estrelas que cintilam sozinhas, presente em todas as telas.
- **Paleta neon:** ciano (`#00ffcc`) como cor de ação principal, roxo (`#b967ff`) para ações secundárias e vermelho-rosa para ações destrutivas/voltar.
- **Tipografia:** fonte `Consolas`, remetendo a um terminal/painel de nave.
- **Painéis flutuantes:** os cards de conteúdo (splash, menus, mesa de edição) ficam sobrepostos ao fundo estrelado, com borda neon e cantos arredondados.
- **Mesa de edição em "cockpit":** menu lateral de filtros + a foto exibida dentro de uma moldura neon (efeito "janela de nave"), que se redimensiona mantendo a proporção original da imagem.

Toda a estilização fica centralizada em `Utils/Tema.py` — cores, fontes e os componentes visuais reutilizáveis (fundo estrelado, painéis, estilos de botão).

## 🚀 Funcionalidades Atuais

- **Navegação Fluida:** Splash screen dinâmica e transição leve entre telas.
- **Interface Moderna:** Construída em Dark Mode com tema espacial, utilizando a biblioteca `customtkinter`.
- **Importação Flexível:**
  - Seleção de imagens direto dos arquivos do computador.
  - Captura de fotos em tempo real usando a webcam.
- **Mesa de Edição (Em construção):** Estrutura preparada para receber os algoritmos matemáticos e filtros personalizados (escala de cinza, desfoque, detecção de bordas).

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)**
- **[OpenCV](https://opencv.org/) (`cv2`)** - O motor principal para leitura e processamento computacional das imagens.
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** - Criação da GUI responsiva e estilizada.
- **[Pillow](https://pillow.readthedocs.io/en/stable/) (`PIL`)** - Conversão e renderização das imagens geradas pelo OpenCV para a interface gráfica.

## 📁 Estrutura do Projeto

```
Space-Editor/
├── TelaPrincipal.py          # Ponto de entrada — splash screen
├── Controlador.py            # Lógica auxiliar de controle
├── Interfaces/
│   ├── TelaInicial.py        # Tela de boas-vindas
│   ├── TelaImportacao.py     # Seleção de arquivo ou webcam
│   └── TelaEdicao.py         # Mesa de edição e filtros
├── Models/
│   └── OpenCv.py             # Funções de captura e processamento de imagem
└── Utils/
    └── Tema.py               # Cores, fontes e componentes visuais compartilhados
```

## ⚙️ Como executar o projeto localmente

1. Clone este repositório para a sua máquina:

```bash
git clone https://github.com/Barrossm/Editor-de-fotos-magistrosas.git
```

2. Acesse a pasta do projeto:

```bash
cd "Editor-de-fotos-magistrosas"
```

3. Instale as bibliotecas necessárias (recomenda-se o uso de um ambiente virtual - `.venv`):

```bash
pip install customtkinter opencv-python pillow
```

4. (Opcional) Salve uma imagem chamada `ellie_espaco.png` na raiz do projeto para aparecer na splash screen. Se o arquivo não existir, um foguete 🚀 é exibido no lugar.

5. Inicie o aplicativo:

```bash
python TelaPrincipal.py
```

## 👨‍💻 Autor

Gabriel Barros de Morais
