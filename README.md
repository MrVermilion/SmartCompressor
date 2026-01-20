# 🚀 Smart Compressor (Image Optimizer)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)]()

> **Select Language / Selecione o Idioma:**
> 
> [🇺🇸 English](#-english) | [🇧🇷 Português](#-português)

---

<div id="english"></div>

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
    git clone [https://github.com/SEU-USUARIO/smart-compressor.git](https://github.com/SEU-USUARIO/smart-compressor.git)
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

### 📂 Project Structure

```text
/smart-compressor
│
├── app.py              # Main application entry point (Flask)
├── redutor.py          # (Optional) Standalone script logic
├── requirements.txt    # Project dependencies
├── .gitignore          # Files to ignore in Git
│
├── static/             # Static files (CSS, JS, Images)
│   └── style.css
│
├── templates/          # HTML Templates
│   └── index.html
│
└── uploads/            # Temporary storage (Auto-generated)
