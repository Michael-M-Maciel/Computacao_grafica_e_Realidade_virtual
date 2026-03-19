import cv2
import numpy as np

# — Criar imagem sintética (sem precisar de arquivo)
img = np.zeros((480, 640, 3), dtype=np.uint8)  # fundo preto
print(f'Shape: {img.shape}')  # (480, 640, 3) = altura, largura, canais

# — Pintar regiões
img[0:240, 0:320] = (255, 0, 0)     # azul (BGR!)
img[0:240, 320:640] = (0, 255, 0)   # verde
img[240:480, 0:320] = (0, 0, 255)   # vermelho
img[240:480, 320:640] = (128, 128, 128)  # cinza

# — Desenhar formas
# Círculo
cv2.circle(img, (320, 240), 80, (255, 255, 0), thickness=3)

# Retângulo
cv2.rectangle(img, (100, 100), (250, 200), (255, 255, 255), thickness=2)

# Linha
cv2.line(img, (0, 0), (640, 480), (0, 255, 255), thickness=2)

# Texto
cv2.putText(img, "Computacao Grafica - UNIFG",
            (160, 460), cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (255, 255, 255), 2)

# — Salvar
cv2.imwrite('/tmp/aula09_basico.png', img)
print('Salva em /tmp/aula09_basico.png')

# — Exibir (se tiver display)
cv2.imshow('Imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()