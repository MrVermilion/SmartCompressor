import os
from flask import Flask, render_template, request, send_file
from PIL import Image

app = Flask(__name__)

# Configura pastas
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- FUNÇÃO DE REDUÇÃO INTEGRADA ---
def reduzir_imagem_inteligente(caminho_entrada, caminho_saida, max_resolution, qualidade_jpeg):
    imagem = Image.open(caminho_entrada)
    
    # 1. Redimensionar (Se o usuário não escolheu 'original')
    if max_resolution != 'original':
        max_res_int = int(max_resolution)
        if imagem.width > max_res_int:
            proporcao = max_res_int / float(imagem.width)
            altura_nova = int((float(imagem.height) * float(proporcao)))
            imagem = imagem.resize((max_res_int, altura_nova), Image.Resampling.LANCZOS)
            print(f"Redimensionado para: {max_res_int}px de largura")

    # 2. Converter para RGB se necessário (para salvar como JPG)
    if imagem.mode in ("RGBA", "P"):
        imagem = imagem.convert("RGB")

    # 3. Salvar com a qualidade escolhida
    imagem.save(caminho_saida, "JPEG", optimize=True, quality=qualidade_jpeg)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comprimir', methods=['POST'])
def comprimir():
    if 'imagem' not in request.files:
        return 'Nenhuma imagem enviada', 400
    
    arquivo = request.files['imagem']
    if arquivo.filename == '':
        return 'Nenhuma imagem selecionada', 400

    # PEGA OS DADOS DO FORMULÁRIO HTML
    # Se der erro, usa valores padrão (2000px e 80% qualidade)
    resolucao_form = request.form.get('resolucao', '2000') 
    qualidade_form = int(request.form.get('qualidade', 80))

    # Salva original
    caminho_entrada = os.path.join(UPLOAD_FOLDER, arquivo.filename)
    arquivo.save(caminho_entrada)
    
    # Define saída
    nome_saida = f"reduzida_{arquivo.filename}"
    caminho_saida = os.path.join(UPLOAD_FOLDER, nome_saida)
    
    # Chama a função passando os parâmetros que vieram da tela
    reduzir_imagem_inteligente(caminho_entrada, caminho_saida, resolucao_form, qualidade_form)
    
    # Remove a original para privacidade
    os.remove(caminho_entrada)
    
    return send_file(caminho_saida, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)