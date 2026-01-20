# 🚀 Smart Compressor (Image Optimizer)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)]()

> **Select Language / Selecione o Idioma:**
> 
> [🇺🇸 English](#english) | [🇧🇷 Português](#portuguese)

---

<a name="english"></a>
## 🇺🇸 English

**Smart Compressor** is a web-based tool designed to reduce image file sizes while maintaining visual quality. Built with **Python** and **Flask**, it allows users to customize resolution and compression levels before downloading the optimized file.

### ✨ Features

* **Smart Compression:** Uses the Pillow (PIL) library to optimize JPEG compression.
* **Intelligent Resizing:** Automatically downscales high-resolution images to reduce size.
* **Privacy First:** Images are processed locally and deleted immediately after conversion.
* **User Interface:** Clean, responsive dashboard created with HTML5 & CSS3.

### 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Image Processing:** Pillow (PIL)
* **Frontend:** HTML5, CSS3, JavaScript
* **Icons:** Google Material Icons

### 📦 Installation & Usage

Follow these steps to run the project locally:

1.  **Clone the repository** (or download files):
    ```bash
    git clone https://github.com/MrVermilion/SmartCompressor.git
    cd smart-compressor
    ```

2.  **Create and Activate a Virtual Environment:**
    * *Windows:*
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    * *Linux/Mac:*
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install Dependencies:**
    ```bash
    pip install flask pillow
    # Or if you have requirements.txt:
    # pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    python app.py
    ```

5.  **Access:**
    Open your browser and go to: `http://127.0.0.1:5000`


<a name="portuguese"></a>
## br Português

# 🚀 Smart Compressor (Otimizador de Imagens)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/Status-Ativo-green.svg)]()

**Smart Compressor** é uma ferramenta web desenvolvida para reduzir o tamanho de arquivos de imagem mantendo a qualidade visual. Construído com **Python** e **Flask**, o sistema permite que o usuário personalize a resolução e o nível de compressão antes de baixar o arquivo otimizado.

---

### ✨ Funcionalidades

* **Compressão Inteligente:** Utiliza a biblioteca Pillow (PIL) para otimizar a compressão JPEG e reduzir drasticamente o tamanho do arquivo.
* **Redimensionamento Automático:** Detecta imagens de altíssima resolução e permite redimensioná-las (ex: Full HD, Web, Mobile) para economizar ainda mais espaço.
* **Privacidade Total:** As imagens são processadas localmente no servidor e deletadas imediatamente após a conversão. Nenhum dado é armazenado.
* **Interface Moderna:** Dashboard limpo, intuitivo e responsivo criado com HTML5 & CSS3.

### 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3, Flask (Micro-framework)
* **Processamento de Imagem:** Pillow (PIL)
* **Frontend:** HTML5, CSS3, JavaScript
* **Ícones:** Google Material Icons

### 📦 Instalação e Uso

Siga os passos abaixo para rodar o projeto na sua máquina:

1.  **Clone o repositório** (ou baixe os arquivos):
    ```bash
    git clone https://github.com/MrVermilion/SmartCompressor.git
    cd smart-compressor
    ```

2.  **Crie e Ative um Ambiente Virtual:**
    * *No Windows:*
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    * *No Linux/Mac:*
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Instale as Dependências:**
    ```bash
    pip install flask pillow
    # Ou se você gerou o arquivo de requisitos:
    # pip install -r requirements.txt
    ```

4.  **Execute a Aplicação:**
    ```bash
    python app.py
    ```

5.  **Acesse:**
    Abra seu navegador e digite: `http://127.0.0.1:5000`

### 📂 Estrutura do Projeto

```text
/smart-compressor
│
├── app.py              # Arquivo principal da aplicação (Flask)
├── redutor.py          # (Opcional) Lógica do script standalone
├── requirements.txt    # Dependências do projeto
├── .gitignore          # Arquivos ignorados pelo Git
│
├── static/             # Arquivos estáticos (CSS, JS, Imagens)
│   └── style.css
│
├── templates/          # Templates HTML
│   └── index.html
│
└── uploads/            # Armazenamento temporário (Gerado automaticamente)
