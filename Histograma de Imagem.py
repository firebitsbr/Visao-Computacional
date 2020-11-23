# Livro VISÃO COMPUTACIONAL EM PYTHON - FERNANDO FELTRIN https://www.amazon.com.br/dp/B08NTW8TNV

import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread('stephenh.jpg', 1)
plt.imshow(imagem)

plt.hist(imagem.ravel(), 256, [0,256])
plt.show()

# Livro Python do ZERO à Programação Orientada a Objetos - https://www.amazon.com.br/dp/B07P2VJVW5
# Livro Programação Orientada a Objetos com Python - https://www.amazon.com.br/dp/B083ZYRY9C
# Livro Tópicos Avançados em Python - https://www.amazon.com.br/dp/B08FBKBC9H
# Livro Ciência de Dados e Aprendizado de Máquina - https://www.amazon.com.br/dp/B07X1TVLKW
# Livro Inteligência Artificial com Python - Redes Neurais Intuitivas - https://www.amazon.com.br/dp/B087YSVVXW
# Livro Redes Neurais Artificiais - https://www.amazon.com.br/dp/B0881ZYYCJ
# Livro Análise Financeira com Python - https://www.amazon.com.br/dp/B08B6ZX6BB
# Livro Arrays com Python + Numpy - https://www.amazon.com.br/dp/B08BTN6V7Y
# Livro Visão Computacional em Python - https://www.amazon.com.br/dp/B08NTW8TNV
