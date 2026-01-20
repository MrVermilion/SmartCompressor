import os
from PIL import Image

def reduzir_imagem_inteligente(caminho_entrada, caminho_saida, tamanho_max_mb=1):
    if not os.path.exists(caminho_entrada):
        print(f"ERRO: Arquivo '{caminho_entrada}' não encontrado.")
        return

    imagem = Image.open(caminho_entrada)
    
    # 1. TÉCNICA DE REDIMENSIONAMENTO (RESIZE)
    # Se a imagem for muito larga (maior que 2000px), reduzimos ela primeiro.
    # Isso ajuda MUITO a baixar o peso sem destruir a qualidade visual.
    largura_maxima = 2000 
    if imagem.width > largura_maxima:
        proporcao = largura_maxima / float(imagem.width)
        altura_nova = int((float(imagem.height) * float(proporcao)))
        imagem = imagem.resize((largura_maxima, altura_nova), Image.Resampling.LANCZOS)
        print(f"Redimensionando para: {largura_maxima}x{altura_nova}px")

    # 2. TÉCNICA DE COMPRESSÃO (LOOP)
    qualidade = 95
    tamanho_alvo = tamanho_max_mb * 500 * 500 
    
    while True:
        # Se precisar converter para RGB (caso seja PNG com fundo transparente, por exemplo)
        if imagem.mode in ("RGBA", "P"):
            imagem = imagem.convert("RGB")

        imagem.save(caminho_saida, "JPEG", optimize=True, quality=qualidade)
        
        tamanho_atual = os.path.getsize(caminho_saida)
        print(f"Qualidade: {qualidade}% | Tamanho: {tamanho_atual/500/500:.2f} MB")
        
        # Condição de parada: Tamanho ok OU qualidade muito baixa
        if tamanho_atual <= tamanho_alvo or qualidade <= 10:
            break
            
        qualidade -= 5

# --- CONFIGURAÇÃO ---
arquivo_original = "Favicon1.jpg"      # Certifique-se que o nome está igual ao da pasta
arquivo_final = "Favicon3.jpg"

reduzir_imagem_inteligente(arquivo_original, arquivo_final)
print("Processo finalizado!")