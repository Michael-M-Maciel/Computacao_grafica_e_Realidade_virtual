import cv2
import numpy as np

# — Ler imagem
img = cv2.imread('render-cg.png')  # render do Blender

if img is None:
    # Criar imagem sintética para o lab
    img = np.random.randint(0, 255, (540, 960, 3), dtype=np.uint8)
    cv2.imwrite('render-cg.png', img)
    img = cv2.imread('render-cg.png')

print(f'Shape: {img.shape}')       # (altura, largura, 3)
print(f'Dtype: {img.dtype}')      # uint8
print(f'Min/Max: {img.min()}/{img.max()}')

# — Recortar (crop)
recorte = img[100:300, 200:500]   # [y_ini:y_fim, x_ini:x_fim]
cv2.imwrite('crop.png', recorte)

# — Redimensionar
pequena = cv2.resize(img, (320, 180))
grande = cv2.resize(img, (1920, 1080), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('pequena.png', pequena)

# — Espelhar
flip_h = cv2.flip(img, 1)  # horizontal (1), vertical (0), ambos (-1)

# — Converter espaço de cor
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv   = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb   = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # para matplotlib

print(f'\nCinza shape: {cinza.shape}')  # (h, w) - 1 canal
print(f'HSV shape: {hsv.shape}')       # (h, w, 3) - H, S, V

# — Histograma de canais
for i, canal in enumerate(['Azul (B)', 'Verde (G)', 'Vermelho (R)']):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    print(f'Canal {canal}: máx={hist.max():.0f} no valor={hist.argmax()}')