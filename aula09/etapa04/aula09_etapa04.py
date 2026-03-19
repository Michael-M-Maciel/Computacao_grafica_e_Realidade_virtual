import cv2
import numpy as np

# O nome do arquivo foi ajustado para bater EXATAMENTE com o que está na sua pasta
caminho_imagem = 'C:/Users/Michael Maciel/OneDrive/Documentos/Michael/UNIFG/Computacao_grafica_e_realidade_virtual/exec_opencv/aula09/blender_render####.png'
caminho_resultado = 'C:/Users/Michael Maciel/OneDrive/Documentos/Michael/UNIFG/Computacao_grafica_e_realidade_virtual/exec_opencv/aula09/resultado_final.png'

print(f"Tentando ler a imagem em: {caminho_imagem}")
img = cv2.imread(caminho_imagem)

if img is None:
    print("ERRO: O arquivo ainda não foi encontrado.")
else:
    print("Imagem encontrada! Aplicando efeitos...")
    
    # Adicionar marca d’água (Texto)
    cv2.putText(img, 'Michael_imagem', (20, 520),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)

    # Realçar bordas (Filtro Canny para criar um estilo desenho)
    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bordas = cv2.Canny(cinza, 30, 100)
    
    # Converter as bordas (1 canal) de volta para cores (3 canais) para misturar
    bordas_bgr = cv2.cvtColor(bordas, cv2.COLOR_GRAY2BGR)
    
    # Misturar a imagem original com as bordas destacadas
    resultado = cv2.addWeighted(img, 0.85, bordas_bgr, 0.15, 0)

    # Salvar resultado final na mesma pasta
    cv2.imwrite(caminho_resultado, resultado)
    print(f"Sucesso! Resultado salvo em: {caminho_resultado}")